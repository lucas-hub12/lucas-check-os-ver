from lucas_check_os_ver.osver import get_os_pretty_name

def test_first():
    v = get_os_pretty_name()
    assert v is not None
    assert v == "Ubuntu 24.04.1 LTS"
    # 빈문자열이 아닌지
    assert v != ""
    # 문자열에 LTS가 포함되었는지
    assert "LTS" in v
    # 문자열에 문자도 있고, 숫자도 있는지
    assert any(c.isalpha() for c in v)
    assert any(c.isdigit() for c in v)
    # . 이 포함되어있는지
    assert "." in v
    # 길이가 적어도 7 이상인지 확인
    assert len(v) >= 7
    # 기타 등등 ...

