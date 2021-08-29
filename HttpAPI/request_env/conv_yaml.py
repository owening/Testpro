import yaml


def test_yaml():
    env = {
        "default": "test",
        "test-env":
            {
                "dev": "127.0.0.2",
                "test": "127.0.0.1",
                "pre": "127.0.0.3"
            }
    }
    with open("env.yaml","w") as f:
        yaml.safe_dump(data=env,stream=f)