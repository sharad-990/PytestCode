import pytest
import yaml

@pytest.fixture
def getValue():
   yaml_path = "C:\\Users\\SharadKumar\\OneDrive - Round the clock technologies\\Desktop\\Test_Google\\test\properties.yaml"
   with open(yaml_path,"r") as file:
      data = yaml.safe_load(file)
      print(data)
   return data

# def getValue(key):