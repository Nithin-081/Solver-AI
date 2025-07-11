import json

def handler(request):
    # Example: echo back a message
    body = request.body.decode()
    data = json.loads(body) if body else {}
    message = data.get('message', 'Hello from Vercel Python API!')
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({'reply': message})
    }
