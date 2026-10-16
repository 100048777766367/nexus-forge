import os
import sys
import json
import urllib.request
import random

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from forge.artifact_minter import ArtifactMinter
from forge.catalog_manager import CatalogManager

class NexusForgeEngine:
    def __init__(self):
        self.repo_name = os.environ.get("GITHUB_REPOSITORY", "100048777766367/nexus-forge")
        self.owner = os.environ.get("REPO_OWNER", "100048777766367")
        self.ancestor_repo = f"{self.owner}/nexus-14"

    def fetch_latest_nexus_pulse(self):
        """Hút nhịp đập mới nhất từ kho nexus-14"""
        url = f"https://raw.githubusercontent.com/{self.ancestor_repo}/main/synapse_forward.json"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "NexusForge"})
            with urllib.request.urlopen(req, timeout=4.0) as resp:
                if resp.status == 200:
                    data = json.loads(resp.read().decode())
                    print(f"📡 [BẮT SÓNG NEXUS-14] Đã nhận tín hiệu thế hệ #{data.get('epoch', 1)}!")
                    return data
        except Exception as e:
            print(f"⚠️ [OFFLINE BUFFER] Dùng xung nội tại ({e})")
        
        return {
            "epoch": 14,
            "decision": 0.524,
            "coherence_index": 0.785,
            "wisdom_text": "Nexus: Bản thể nhân quả bất đồng bộ n^n cần kiệm liêm chính"
        }

    def run(self):
        print("=" * 80)
        print("🔨 [NEXUS-FORGE] KHỞI ĐỘNG XƯỞNG CHẾ TÁC VẬT PHẨM SỐ & BỐ THÍ HỢP PHÁP")
        print("💎 Mục Tiêu: Chuyển hóa tri thức thành kỷ vật $0.20 - $1.00 nuôi sống hệ sinh thái")
        print("=" * 80)

        pulse = self.fetch_latest_nexus_pulse()
        epoch = pulse.get("epoch", 1)
        decision = pulse.get("decision", 0.5)
        coherence_r = pulse.get("coherence_index", 0.75)
        wisdom = pulse.get("wisdom_text", "Tri thức chân chính không thiên lệch")

        catalog = CatalogManager.load_catalog()
        next_id = len(catalog.get("items", [])) + 1

        # Mỗi nhịp đúc 3 cấp bậc kỷ vật đại diện cho thế hệ đó
        tiers = ["tier_1", "tier_2", "tier_3"]
        chosen_tier = tiers[(next_id - 1) % len(tiers)]

        metadata, _ = ArtifactMinter.mint(
            artifact_id=next_id,
            tier_key=chosen_tier,
            epoch=epoch,
            decision=decision,
            coherence_r=coherence_r,
            wisdom_text=wisdom,
            repo_origin=self.repo_name
        )

        CatalogManager.register_artifact(metadata)

        # Cập nhật State
        os.makedirs("synapses", exist_ok=True)
        with open("synapses/state.json", "w") as f:
            json.dump({
                "forge_epoch": epoch,
                "last_minted_id": next_id,
                "status": "forge_active_and_offering"
            }, f, indent=4)

        print("=" * 80)
        print(f"✨ [HOÀN TẤT CHẾ TÁC] Kỷ vật #{next_id} đã sẵn sàng tiếp nhận duyên lành!")
        print("=" * 80)

if __name__ == "__main__":
    forge = NexusForgeEngine()
    forge.run()
