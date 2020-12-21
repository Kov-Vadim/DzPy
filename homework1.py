def my_function(str1:str,bool1:bool):
    my_str = "=!@#$%&*/-+?,.]}"
    if not bool1:
        str1 = str1[::-1]
    for index, value_key in enumerate(str1):
        my_bool = False
        for value_str in my_str:
            if value_key == value_str:
                my_bool = True
        if not my_bool:
            key_index1 = index
            break
    if bool1:
        key_index2 = my_function(str1,False)
        key_index2 = len(str1) - key_index2
        return key_index1,key_index2
    else:
        return key_index1


def parse(query: str) -> dict:
    my_dict = {}
    my_list = []
    if query.rfind("?") != -1:
        my_index = query.find("?")
        query = query[my_index+1:]
        if query != "":
            if query.rfind("&") != -1:
                my_list = query.split("&")
            else:
                my_list += [query]
            for value in my_list:
                if value != "" and value.rfind("=") != -1:
                    my_index = value.find("=")
                    my_key = value[:my_index]
                    key_index1,key_index2 = my_function(my_key, True)
                    my_key = my_key[key_index1:key_index2]
                    my_default = value[my_index+1:].strip()
                    default_index1, default_index2 = my_function(my_default, True)
                    my_default = my_default[default_index1:default_index2]
                    my_dict.update({my_key: my_default})
    return my_dict


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('http://example.com/?sdfghu') == {}
    assert parse('dfghjhgfhu') == {}
    assert parse('http://example.com/?name===Dima') == {'name': 'Dima'}
    assert parse('http://example.com/?#$%&*name=Dima$%&*/') == {'name': 'Dima'}
    assert parse('http://example.com/?имя=Дима') == {'имя': 'Дима'}


def parse_cookie(query: str) -> dict:
    my_dict = {}
    my_list = []
    my_bool = False
    if query.rfind(";") != -1:
        my_list = query.split(";")
    else:
        my_list += [query]
    if query != "":
        for value in my_list:
            if value != "" and value.rfind("=") != -1:
                my_index = value.find("=")
                my_key = value[:my_index].strip()
                key_index1,key_index2 = my_function(my_key, True)
                my_key = my_key[key_index1:key_index2]
                my_default = value[my_index+1:].strip()
                default_index1, default_index2 = my_function(my_default, True)
                my_default = my_default[default_index1:default_index2]
                my_dict.update({my_key:my_default})
    return my_dict


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('profession=programmer') == {'profession': 'programmer'}
    assert parse_cookie('dfghjyl') == {}
    assert parse_cookie('имя=Дима') == {'имя': 'Дима'}
    assert parse_cookie('  name =     Dima') == {'name': 'Dima'}
    assert parse_cookie('*/-+?name!@#$=%Dima,.]}') == {'name': 'Dima'}
    assert parse_cookie('name===Dima;') == {'name': 'Dima'}