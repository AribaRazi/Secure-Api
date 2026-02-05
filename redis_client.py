# import redis
# import os

# r = redis.Redis(
#     host="localhost",
#     port=6379,
#     decode_responses=True
# )
import redis
import os

r = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=(os.getenv("REDIS_PORT")),
    decode_responses=True
)

