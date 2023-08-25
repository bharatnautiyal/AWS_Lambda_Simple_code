import json

def lambda_handler(event, context):
    # TODO implement
    
    body = '''
    <!DOCTYPE html>
<html>
<head>
    <title>Hello, Bharat!</title>

    <h1>Are you Robert Downey Jr ?</h1>
    <img src="https://thehardtimes.net/wp-content/uploads/2020/10/tony-stark.jpg" alt="Image">
    <h1> I .  AM . <a href="blob">  IRONMAN  </a></h1>

</body>
</html>'''
    
    
    response = {
        'statusCode': 200,
        'headers' : {"Content-type":"text/html",},
        'body': body
    }

    return response
