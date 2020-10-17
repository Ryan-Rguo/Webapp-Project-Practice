import asyncio
import orm
from models import User, Blog, Comment

loop = asyncio.get_event_loop()

async def test():
    await orm.create_pool(loop=loop, user='www-data', password='www-data', db='awesome')

    u = User(name='Ryan', email='ryan@example.com', passwd='11111111', image='about:blank')

    await u.save()

loop.run_until_complete(test())