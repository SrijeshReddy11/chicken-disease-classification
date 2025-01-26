import sys
print("Python path:")
print(sys.path)
print("\nTrying to import...")

try:
    import cnnClassifier
    print(f"cnnClassifier location: {cnnClassifier.__file__}")
    
    from cnnClassifier.constants import CONFIG_FILE_PATH
    print(f"CONFIG_FILE_PATH: {CONFIG_FILE_PATH}")
except Exception as e:
    print(f"Error occurred: {str(e)}") 