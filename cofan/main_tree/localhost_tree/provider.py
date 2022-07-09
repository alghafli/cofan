from pathlib import Path

def provider(env):
  if Path(env['root']).is_file():
    browser_cls = env['providers'].Ziper
    upload = False
  else:
    browser_cls = env['providers'].Filer
    upload = bool(env['upload_password'])
  
  if upload:
    return browser_cls(env['root'], iconer=env['providers'].Iconer(),
      tfman=env['tfman']())
  else:
    return browser_cls(env['root'], iconer=env['providers'].Iconer())

