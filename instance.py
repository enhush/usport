# -*- coding: utf-8 -*-

from usport.app import create_app
from usport.settings import DevConfig, ProdConfig

CONFIG = DevConfig  # ProdConfig

app = create_app(CONFIG)

if __name__ == '__main__':
    app.run(debug=CONFIG.DEBUG, host='0.0.0.0')
