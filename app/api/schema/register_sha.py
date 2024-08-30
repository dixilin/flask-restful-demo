def register_args_valid(parser):
    parser.add_argument('username', type=str, required=True, location = 'json')
    parser.add_argument('pwd', type=str, required=True, location = 'json')

    # 这种方式也行
    # args = {
    #     'username': {'type': str, 'required': True, 'location': 'json'},
    #     'pwd': {'type': str, 'required': True, 'location': 'json'}
    # }
    # parser.add_args(args)
