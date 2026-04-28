# gunicorn.conf.py — configuração do servidor de produção
bind = "0.0.0.0:8000"
workers = 2
timeout = 120
forwarded_allow_ips = "*"
loglevel = "info"
accesslog = "-"
errorlog = "-"
