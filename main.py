from livekit import api

api_key = "devkey"
api_secret = "secret"

room_name = "test-room"
identity = "user1"

token = api.AccessToken(api_key, api_secret)
token.with_identity(identity)
token.with_grants(api.VideoGrants(
    room_join=True,
    room=room_name,
))

print(token.to_jwt())