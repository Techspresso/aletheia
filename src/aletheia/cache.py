import redis
from redis_lru import RedisLRU

client = redis.StrictRedis()
cache = RedisLRU(client)