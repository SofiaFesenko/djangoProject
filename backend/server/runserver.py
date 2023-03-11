import os
from pathlib import Path

import uvicorn


if __name__ == "__main__":
    """Django 3 does not support lifespan protocol. If you need to use lifespan signals use django signals natively"""
    reload_dir = Path(__file__).resolve().parent.parent  # /backend/
    uvicorn.run(
        'server.asgi:asgi_app',
        host="0.0.0.0", port=8080,
        reload=bool(os.environ.get('RELOAD_AFTER_CODE_CHANGES', False)),
        reload_dirs=[reload_dir]
    )
