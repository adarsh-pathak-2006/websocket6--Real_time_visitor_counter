from channels.generic.websocket import AsyncWebsocketConsumer
import json

class CounterConsumer(AsyncWebsocketConsumer):
    user_counter=0
    async def connect(self):
        await self.accept()
        try:
            self.user=self.scope["user"]
            if self.user.is_authenticated:
                self.group_name="group"
                await self.channel_layer.group_add(self.group_name, self.channel_name)
                CounterConsumer.user_counter=CounterConsumer.user_counter+1
                await self.channel_layer.group_send(self.group_name, {
                    'type':'user_count',
                    'count':CounterConsumer.user_counter,    
                })
            else:
                await self.send(text_data=json.dumps({'error': 'User is not authenticated'}))
                await self.close()
        except Exception as e:
            await self.send(text_data=json.dumps({'error': str(e)}))
            await self.close()

    async def user_count(self, event):
        await self.send(text_data=json.dumps({ 'count': event["count"] }))

    async def disconnect(self, code):
        if not hasattr(self, "group_name"):
            return
        CounterConsumer.user_counter=CounterConsumer.user_counter-1
        await self.channel_layer.group_send(self.group_name, {
            'type':'user_count',
            'count':CounterConsumer.user_counter,    
        })
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        
        