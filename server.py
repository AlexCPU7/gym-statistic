import aiohttp
import asyncio
import argparse
from demo import create_app
from demo.settings import load_config

try:  
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    print('Library uvloop is not available')

parser = argparse.ArgumentParser(description='Parsing project')
parser.add_argument('--host', help='Host to listen', default='0.0.0.0')
parser.add_argument('--port', help='Port to accept connections', default=8080)
parser.add_argument('--reload', action='store_true', help='Autoreload code on change')
parser.add_argument('-c', '--config', type=argparse.FileType('r'), help='Path to configuration file')
args = parser.parse_args()

app = create_app(config=load_config(args.config))

if args.reload:
    import aioreloader
    aioreloader.start()
    print('Start with code reload')

if __name__ == '__main__':
    aiohttp.web.run_app(app, host=args.host, port=args.port)