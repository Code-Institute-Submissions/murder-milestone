{"filter":false,"title":"settings.py","tooltip":"/murder_mystery/settings.py","undoManager":{"mark":54,"position":54,"stack":[[{"start":{"row":27,"column":17},"end":{"row":27,"column":86},"action":"insert","lines":["'9789e65bcf9840e8a867634f1b3a45a8.vfs.cloud9.us-east-1.amazonaws.com'"],"id":6}],[{"start":{"row":27,"column":18},"end":{"row":27,"column":85},"action":"remove","lines":["9789e65bcf9840e8a867634f1b3a45a8.vfs.cloud9.us-east-1.amazonaws.com"],"id":7},{"start":{"row":27,"column":18},"end":{"row":27,"column":19},"action":"insert","lines":["o"]},{"start":{"row":27,"column":19},"end":{"row":27,"column":20},"action":"insert","lines":["s"]},{"start":{"row":27,"column":20},"end":{"row":27,"column":21},"action":"insert","lines":["."]},{"start":{"row":27,"column":21},"end":{"row":27,"column":22},"action":"insert","lines":["e"]},{"start":{"row":27,"column":22},"end":{"row":27,"column":23},"action":"insert","lines":["n"]}],[{"start":{"row":27,"column":23},"end":{"row":27,"column":24},"action":"insert","lines":["v"],"id":8},{"start":{"row":27,"column":24},"end":{"row":27,"column":25},"action":"insert","lines":["i"]},{"start":{"row":27,"column":25},"end":{"row":27,"column":26},"action":"insert","lines":["r"]},{"start":{"row":27,"column":26},"end":{"row":27,"column":27},"action":"insert","lines":["o"]},{"start":{"row":27,"column":27},"end":{"row":27,"column":28},"action":"insert","lines":["n"]},{"start":{"row":27,"column":28},"end":{"row":27,"column":29},"action":"insert","lines":["."]},{"start":{"row":27,"column":29},"end":{"row":27,"column":30},"action":"insert","lines":["g"]},{"start":{"row":27,"column":30},"end":{"row":27,"column":31},"action":"insert","lines":["e"]}],[{"start":{"row":27,"column":31},"end":{"row":27,"column":32},"action":"insert","lines":["t"],"id":9}],[{"start":{"row":27,"column":32},"end":{"row":27,"column":33},"action":"insert","lines":["("],"id":10}],[{"start":{"row":27,"column":17},"end":{"row":27,"column":18},"action":"remove","lines":["'"],"id":11}],[{"start":{"row":27,"column":32},"end":{"row":27,"column":33},"action":"remove","lines":["'"],"id":12}],[{"start":{"row":27,"column":32},"end":{"row":27,"column":33},"action":"insert","lines":["C"],"id":13},{"start":{"row":27,"column":33},"end":{"row":27,"column":34},"action":"insert","lines":["9"]},{"start":{"row":27,"column":34},"end":{"row":27,"column":35},"action":"insert","lines":["_"]},{"start":{"row":27,"column":35},"end":{"row":27,"column":36},"action":"insert","lines":["H"]}],[{"start":{"row":27,"column":36},"end":{"row":27,"column":37},"action":"insert","lines":["O"],"id":14},{"start":{"row":27,"column":37},"end":{"row":27,"column":38},"action":"insert","lines":["T"]}],[{"start":{"row":27,"column":37},"end":{"row":27,"column":38},"action":"remove","lines":["T"],"id":15}],[{"start":{"row":27,"column":37},"end":{"row":27,"column":38},"action":"insert","lines":["S"],"id":16},{"start":{"row":27,"column":38},"end":{"row":27,"column":39},"action":"insert","lines":["T"]},{"start":{"row":27,"column":39},"end":{"row":27,"column":40},"action":"insert","lines":["N"]},{"start":{"row":27,"column":40},"end":{"row":27,"column":41},"action":"insert","lines":["A"]},{"start":{"row":27,"column":41},"end":{"row":27,"column":42},"action":"insert","lines":["M"]},{"start":{"row":27,"column":42},"end":{"row":27,"column":43},"action":"insert","lines":["E"]}],[{"start":{"row":27,"column":43},"end":{"row":27,"column":44},"action":"insert","lines":["'"],"id":17}],[{"start":{"row":27,"column":32},"end":{"row":27,"column":33},"action":"insert","lines":["'"],"id":18}],[{"start":{"row":27,"column":45},"end":{"row":27,"column":46},"action":"insert","lines":[")"],"id":19}],[{"start":{"row":27,"column":17},"end":{"row":27,"column":46},"action":"remove","lines":["os.environ.get('C9_HOSTNAME')"],"id":20},{"start":{"row":27,"column":17},"end":{"row":27,"column":86},"action":"insert","lines":["'9789e65bcf9840e8a867634f1b3a45a8.vfs.cloud9.us-east-1.amazonaws.com'"]}],[{"start":{"row":120,"column":23},"end":{"row":121,"column":0},"action":"insert","lines":["",""],"id":21},{"start":{"row":121,"column":0},"end":{"row":122,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":122,"column":0},"end":{"row":122,"column":74},"action":"insert","lines":["MESSAGE_STORAGE = \"django.contrib.messages.storage.session.SessionStorage\""],"id":22}],[{"start":{"row":57,"column":8},"end":{"row":57,"column":19},"action":"remove","lines":["'DIRS': [],"],"id":23},{"start":{"row":57,"column":8},"end":{"row":57,"column":54},"action":"insert","lines":["'DIRS': [os.path.join(BASE_DIR, 'templates')],"]}],[{"start":{"row":122,"column":74},"end":{"row":123,"column":0},"action":"insert","lines":["",""],"id":24},{"start":{"row":123,"column":0},"end":{"row":124,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":124,"column":0},"end":{"row":124,"column":64},"action":"insert","lines":["EMAIL_BACKEND = \"django.core.mail.backends.console.EmailBackend\""],"id":25}],[{"start":{"row":124,"column":0},"end":{"row":124,"column":1},"action":"insert","lines":["#"],"id":26}],[{"start":{"row":125,"column":0},"end":{"row":126,"column":0},"action":"insert","lines":["",""],"id":27}],[{"start":{"row":126,"column":0},"end":{"row":130,"column":16},"action":"insert","lines":["EMAIL_USE_TLS = True","EMAIL_HOST = 'smtp.gmail.com'","EMAIL_HOST_USER = os.environ.get(\"EMAIL_ADDRESS\")","EMAIL_HOST_PASSWORD = os.environ.get(\"EMAIL_PASSWORD\")","EMAIL_PORT = 587"],"id":28}],[{"start":{"row":124,"column":0},"end":{"row":124,"column":1},"action":"remove","lines":["#"],"id":29}],[{"start":{"row":130,"column":16},"end":{"row":131,"column":0},"action":"insert","lines":["",""],"id":30},{"start":{"row":131,"column":0},"end":{"row":132,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":132,"column":0},"end":{"row":135,"column":1},"action":"insert","lines":["AUTHENTICATION_BACKENDS = [","    'django.contrib.auth.backends.ModelBackend',","    'accounts.backends.EmailAuth'","]"],"id":31}],[{"start":{"row":39,"column":15},"end":{"row":40,"column":0},"action":"insert","lines":["",""],"id":32},{"start":{"row":40,"column":0},"end":{"row":40,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":40,"column":4},"end":{"row":40,"column":6},"action":"insert","lines":["''"],"id":33}],[{"start":{"row":40,"column":5},"end":{"row":40,"column":6},"action":"insert","lines":["p"],"id":34},{"start":{"row":40,"column":6},"end":{"row":40,"column":7},"action":"insert","lines":["r"]},{"start":{"row":40,"column":7},"end":{"row":40,"column":8},"action":"insert","lines":["o"]},{"start":{"row":40,"column":8},"end":{"row":40,"column":9},"action":"insert","lines":["d"]},{"start":{"row":40,"column":9},"end":{"row":40,"column":10},"action":"insert","lines":["u"]},{"start":{"row":40,"column":10},"end":{"row":40,"column":11},"action":"insert","lines":["c"]},{"start":{"row":40,"column":11},"end":{"row":40,"column":12},"action":"insert","lines":["t"]},{"start":{"row":40,"column":12},"end":{"row":40,"column":13},"action":"insert","lines":["s"]}],[{"start":{"row":40,"column":14},"end":{"row":40,"column":15},"action":"insert","lines":[","],"id":35}],[{"start":{"row":65,"column":70},"end":{"row":66,"column":0},"action":"insert","lines":["",""],"id":36},{"start":{"row":66,"column":0},"end":{"row":66,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":66,"column":16},"end":{"row":66,"column":58},"action":"insert","lines":["'django.template.context_processors.media'"],"id":37}],[{"start":{"row":66,"column":58},"end":{"row":66,"column":59},"action":"insert","lines":[","],"id":38}],[{"start":{"row":137,"column":1},"end":{"row":138,"column":0},"action":"insert","lines":["",""],"id":39},{"start":{"row":138,"column":0},"end":{"row":139,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":139,"column":0},"end":{"row":140,"column":21},"action":"insert","lines":["MEDIA_ROOT = os.path.join(BASE_DIR, 'media')","MEDIA_URL = '/media/'"],"id":40}],[{"start":{"row":40,"column":15},"end":{"row":41,"column":0},"action":"insert","lines":["",""],"id":41},{"start":{"row":41,"column":0},"end":{"row":41,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":41,"column":4},"end":{"row":41,"column":15},"action":"insert","lines":["'products',"],"id":42}],[{"start":{"row":41,"column":5},"end":{"row":41,"column":12},"action":"remove","lines":["product"],"id":43},{"start":{"row":41,"column":5},"end":{"row":41,"column":6},"action":"insert","lines":["c"]},{"start":{"row":41,"column":6},"end":{"row":41,"column":7},"action":"insert","lines":["a"]},{"start":{"row":41,"column":7},"end":{"row":41,"column":8},"action":"insert","lines":["r"]},{"start":{"row":41,"column":8},"end":{"row":41,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":41,"column":9},"end":{"row":41,"column":10},"action":"remove","lines":["s"],"id":44}],[{"start":{"row":67,"column":59},"end":{"row":68,"column":0},"action":"insert","lines":["",""],"id":45},{"start":{"row":68,"column":0},"end":{"row":68,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":68,"column":16},"end":{"row":68,"column":45},"action":"insert","lines":["'cart.contexts.cart_contents'"],"id":46}],[{"start":{"row":68,"column":45},"end":{"row":68,"column":46},"action":"insert","lines":[","],"id":47}],[{"start":{"row":41,"column":11},"end":{"row":42,"column":0},"action":"insert","lines":["",""],"id":48},{"start":{"row":42,"column":0},"end":{"row":42,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":42,"column":4},"end":{"row":42,"column":6},"action":"insert","lines":["''"],"id":49}],[{"start":{"row":42,"column":5},"end":{"row":42,"column":27},"action":"insert","lines":["django_forms_bootstrap"],"id":50}],[{"start":{"row":42,"column":28},"end":{"row":42,"column":29},"action":"insert","lines":[","],"id":51}],[{"start":{"row":125,"column":0},"end":{"row":125,"column":23},"action":"remove","lines":["STATIC_URL = '/static/'"],"id":52},{"start":{"row":125,"column":0},"end":{"row":128,"column":1},"action":"insert","lines":["STATIC_URL = '/static/'","STATICFILES_DIRS = [","    os.path.join(BASE_DIR, \"static\")","]"]}],[{"start":{"row":146,"column":21},"end":{"row":147,"column":0},"action":"insert","lines":["",""],"id":53},{"start":{"row":147,"column":0},"end":{"row":148,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":148,"column":0},"end":{"row":149,"column":42},"action":"insert","lines":["STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE')","STRIPE_SECRET = os.getenv('STRIPE_SECRET')"],"id":54}],[{"start":{"row":12,"column":9},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":55},{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":["i"]},{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"insert","lines":["m"]},{"start":{"row":13,"column":2},"end":{"row":13,"column":3},"action":"insert","lines":["p"]},{"start":{"row":13,"column":3},"end":{"row":13,"column":4},"action":"insert","lines":["o"]},{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"insert","lines":["r"]},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"insert","lines":[" "],"id":56},{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"insert","lines":["e"]},{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"insert","lines":["n"]},{"start":{"row":13,"column":9},"end":{"row":13,"column":10},"action":"insert","lines":["v"]}],[{"start":{"row":43,"column":29},"end":{"row":44,"column":0},"action":"insert","lines":["",""],"id":57},{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":44,"column":4},"end":{"row":44,"column":6},"action":"insert","lines":["''"],"id":58}],[{"start":{"row":44,"column":5},"end":{"row":44,"column":6},"action":"insert","lines":["c"],"id":59},{"start":{"row":44,"column":6},"end":{"row":44,"column":7},"action":"insert","lines":["h"]},{"start":{"row":44,"column":7},"end":{"row":44,"column":8},"action":"insert","lines":["e"]},{"start":{"row":44,"column":8},"end":{"row":44,"column":9},"action":"insert","lines":["c"]},{"start":{"row":44,"column":9},"end":{"row":44,"column":10},"action":"insert","lines":["k"]},{"start":{"row":44,"column":10},"end":{"row":44,"column":11},"action":"insert","lines":["o"]},{"start":{"row":44,"column":11},"end":{"row":44,"column":12},"action":"insert","lines":["u"]},{"start":{"row":44,"column":12},"end":{"row":44,"column":13},"action":"insert","lines":["t"]}],[{"start":{"row":44,"column":14},"end":{"row":44,"column":15},"action":"insert","lines":[","],"id":60}]]},"ace":{"folds":[],"scrolltop":240,"scrollleft":0,"selection":{"start":{"row":34,"column":27},"end":{"row":34,"column":27},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1586254427080,"hash":"015bff0f50c76751a7b577bb8ab93e63703b311a"}