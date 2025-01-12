from wsgiref.simple_server import make_server
import json
from datetime import datetime
import pytz
from tzlocal import get_localzone

server_time_zone = get_localzone()

def get_current_time(time_zone_name):
    if time_zone_name:
        time_zone = pytz.timezone(time_zone_name)
    else:
        time_zone = server_time_zone
    return datetime.now(time_zone)

def application(environ, start_response):
    path = environ.get('PATH_INFO', '').lstrip('/')
    method = environ['REQUEST_METHOD']

    if method == 'GET':
        if path == '':
            current_time = get_current_time(None)
            response_body = f"<html><body><h1>Current time: {current_time}</h1></body></html>"
            status = '200 OK'
            headers = [('Content-Type', 'text/html')]
        else:
            try:
                current_time = get_current_time(path)
                response_body = f"<html><body><h1>Current time in {path}: {current_time}</h1></body></html>"
                status = '200 OK'
                headers = [('Content-Type', 'text/html')]
            except Exception as e:
                response_body = f"<html><body><h1>Error, {str(e)}</h1></body></html>"
                status = '400 Bad Request'
                headers = [('Content-Type', 'text/html')]
    
    elif method == 'POST':
        try:
            content_length = int(environ.get('CONTENT_LENGTH', 0))
            post_data = environ['wsgi.input'].read(content_length).decode('utf-8')
            data = json.loads(post_data)
            
            if path == 'api/v1/time':
                time_zone = data.get('time_zone')
                current_time = get_current_time(time_zone)
                response_body = json.dumps({'current_time': current_time.isoformat()})
                status = '200 OK'
                headers = [('Content-Type', 'application/json')]
                
            elif path == 'api/v1/date':
                time_zone = data.get('time_zone')
                current_date = get_current_time(time_zone).date()
                response_body = json.dumps({'current_date': current_date.isoformat()})
                status = '200 OK'
                headers = [('Content-Type', 'application/json')]
                
            elif path == 'api/v1/datediff':
                start_date = data.get('start')
                end_date = data.get('end')
                
                start_time_zone = start_date.get('time_zone', str(server_time_zone))
                end_time_zone = end_date.get('time_zone', str(server_time_zone))

                start_time_normal = datetime.strptime(start_date['date'], '%m.%d.%Y %H:%M:%S')
                end_time_normal = datetime.strptime(end_date['date'], '%m.%d.%Y %H:%M:%S')

                start_time = pytz.timezone(start_time_zone).localize(start_time_normal)
                end_time = pytz.timezone(end_time_zone).localize(end_time_normal)

                diff = end_time - start_time
                response_body = json.dumps({'difference': str(diff)})
                status = '200 OK'
                headers = [('Content-Type', 'application/json')]
                
            else:
                response_body = json.dumps({'error': 'Wrong way'})
                status = '404 Not Found'
                headers = [('Content-Type', 'application/json')]
                
        except Exception as e:
            response_body = json.dumps({'error': str(e)})
            status = '400 Bad Request'
            headers = [('Content-Type', 'application/json')]
    
    else:
        response_body = json.dumps({'error': 'Method is not supported'})
        status = '405 Method Not Allowed'
        headers = [('Content-Type', 'application/json')]
    
    start_response(status, headers)
    return [response_body.encode('utf-8')]

if __name__ == '__main__':
    server = make_server('0.0.0.0', 8000, application)
    print("Server is running on  http://localhost:8000")
    server.serve_forever()
