

```
from urlock import urlock.Urlock
import baseconvert
import time
import random
import dumper

zod = Urlock("http://localhost:8080", "lidlut-tabwed-pillex-ridrup")
r = zod.connect()
s = zod.subscribe("zod", "chat-store", "/mailbox/~/~zod/mc")

pipe = zod.sse_pipe()

s = baseconvert.base(random.getrandbits(128), 10, 32, string=True).lower()
uid = '0v' + '.'.join(s[i:i+5] for i in range(0, len(s), 5))[::-1]

p = zod.poke("zod", "chat-hook", "json", {"message": {"path": "/~/~zod/mc",
    "envelope": {"uid": uid,
                                                                    "number": 1,
                                                                    "author": "~zod",
                                                                    "when": int(time.time() * 1000),
                                                                    "letter": {"text": "this shit is new"}}}})


for m in pipe.events():
   dumper.dump(m)
```