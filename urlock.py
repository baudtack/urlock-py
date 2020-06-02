import datetime
import random
import requests
import sseclient

class Urlock():
    def __init__(self, url, code):
        self.uid = str(datetime.datetime.now().timestamp()).split('.', 1)[0] + '-' + random.random().hex()[2:][:-3][-6:]
        self.session = requests.Session()
        self.lastEventId = 0
        self.url = url
        self.code = code
        self.channelUrl = self.url + "/~/channel/" + self.uid
        self.sseclient = False

    def getEventId(self):
        self.lastEventId += 1
        return self.lastEventId 
        
    def connect(self):
        return self.session.post(self.url + '/~/login', data = {'password': self.code})

    def poke(self, ship, app, mark, j):
        res = self.session.put(self.channelUrl,
                               json = [{ 'id': self.getEventId(),
                                         'action': "poke",
                                         'ship': ship,
                                         'app': app,
                                         'mark': mark,
                                         'json': j}])
        return res

    def ack(self, eventId):
       return self.session.put(self.channelUrl, data = { "event-id": eventId })

    def sse_pipe(self):
        if(not self.sseclient):
            self.sseClient = sseclient.SSEClient(self.session.get(self.channelUrl, stream=True))
        return self.sseClient

    def subscribe(self, ship, app, path):
        json = [{'id': self.getEventId(),
                'action': "subscribe",
                'ship': ship,
                'app': app,
                'path': path }]
        return self.session.put(self.channelUrl, json = json)

    def unsubscribe(self, subscription):
        res = self.session.put(self.channelUrl, json = [{'id': self.getEventId(),
                                                         'action': "unsubscribe",
                                                         'subscription': subscription}])
        return res

    def delete(self):
        res = self.session.put(self.channelUrl, json = [{'id': self.getEventId(),
                                                         'action': "delete"}])
        return res
