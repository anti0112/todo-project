from bot.models import TgUser
from bot.tg.dc import Message
from goals.models import Goal
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from tg.client import TgClient



class Command(BaseCommand):
    help = 'run bot'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tg_client = TgClient(settings.TG_TOKEN)
        
        
    def handle_user_verification(self, msg: Message, tg_user: TgUser):
        tg_user.set_verification_code()
        tg_user.save(update_fields=["verification_code"])
        self.tg_client.send_message(
            msg.chat.id, f"[verification_code] {tg_user.verification_code}"
        )
        
    def  fetch_tasks(self, msg: Message, tg_user: TgUser):
        goals = Goal.objects.filter(user=tg_user.user)
        if goals.count > 0:
            resp_msg = [f"{item.id} {item.title}" for item in goals]
            self.tg_client.send_message(msg.chat.id, '\n'.join(resp_msg))
        else:
            self.tg_client.send_message(msg.chat_id, "[you have no goals]")
            
    def handle_verified_user(self, msg: Message, tg_user: TgUser):
        if not msg.text:
            return
        if '/goals' in msg.text:
            self.fetch_tasks(msg, tg_user)
        else:
            self.tg_client.send_message(msg.chat_id, '[unknown command]')
    
    def handle_message(self, msg: Message):
        tg_user, created = TgUser.objects.get_or_create(
            tg_id=msg.from_.id,
            defaults={
                "tg_char_id": msg.chat.id,
                'username': msg.from_.username
            },
        )
        
        if created:
            self.tg_client.send_message(msg.chat.id, '[success]')
            
        if tg_user.user:
            self.handle_verified_user(msg, tg_user)
        else:
            self.handle_user_verification(msg, tg_user)
    
    def handle(self, *args, **kwargs):
        offset = 0
        
        while True:
            res = self.tg_client.get_updates(offset=offset)
            for item in res.result:
                offset = item.update_id + 1
                self.handle_message(item.message)
        