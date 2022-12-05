import redis

# connect to redis
client = redis.Redis(host='0.0.0.0', port=6379)

# set a key
client.set('test-key', 'test-value')

# get a value
value = client.get('test-key')
print(value)
