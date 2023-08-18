import json

def lambda_handler(event, context):
    # TODO implement
    
    body = '''
    <!DOCTYPE html>
<html>
<head>
    <title>Hello, Bharat!</title>
</head>
<body>
    <h1> IRONMAN </h1>
    <img src="https://www.makingacinephile.com/wp-content/uploads/2021/02/baa5e44f5cfe8f939bbbca868454512c5ce449b7.jpg" alt="Image">
</body>
</html>'''
    
    
    response = {
        'statusCode': 200,
        'headers' : {"Content-type":"text/html",},
        'body': body
    }

    return response