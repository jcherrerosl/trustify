import hashlib

def generate_hash(file_path: str):
    with open(file_path, "rb") as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    return file_hash

def check_metadata(file_path: str):
    # Aquí puedes parsear metadata básica (audio, imagen, pdf, etc.)
    return {
        "author": "Unknown",
        "creation_date": "N/A"
    }

def generate_proof(file_path: str):
    return {
        "hash": generate_hash(file_path),
        "metadata": check_metadata(file_path)
    }
