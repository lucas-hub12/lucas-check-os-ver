from lucas_check_os_ver.osver import get_os_pretty_name

def test_first():
    v = get_os_pretty_name()
    assert v is not None
    assert v == "Ubuntu 24.04.1 LTS"
# 빈문자열이 아닌지
# 문자열에 LTS가 포함되었는지
# 문자열에 문자도 있고, 숫자도 있는지
# . 이 포함되어있는지
# 기타 등등 ...
# 길이가 적어도 얼마 이상인지...


