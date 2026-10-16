import hashlib
import json

class ProofAttestation:
    """Tạo chữ ký số mật mã SHAKE-256 xác thực nguồn gốc vật phẩm"""
    @staticmethod
    def generate_proof(artifact_id, epoch, decision, wisdom_text, repo_origin):
        payload = f"{artifact_id}_{epoch}_{decision}_{wisdom_text}_{repo_origin}".encode()
        # Chữ ký bọt biển SHAKE-256 64 bytes
        signature = hashlib.shake_256(payload).hexdigest(32)
        # Băm Merkle Leaf
        leaf_hash = hashlib.sha256(signature.encode()).hexdigest()

        return {
            "signature": f"0x{signature}",
            "merkle_leaf": f"0x{leaf_hash}",
            "origin_canon": repo_origin,
            "verifiable_at": f"https://github.com/{repo_origin}/tree/main/synapses"
        }
