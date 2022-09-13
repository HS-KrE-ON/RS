"""
Test implementation of a Restful API
"""
import os
from website import create_app
import logging

app = create_app()

app.logger.addHandler(logging.StreamHandler(os.system.stdout))
app.logger.setLevel(logging.ERROR)

if __name__=='__main__':
    cfg_port = os.getenv('PORT', "5000")
    app.run(host="0.0.0.0", port=cfg_port)#, debug=True)
#Test
