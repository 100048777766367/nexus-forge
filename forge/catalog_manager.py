import os
import json

CATALOG_FILE = "synapses/catalog.json"
PATRON_FILE = "synapses/patron_registry.json"

class CatalogManager:
    """Quản trị danh mục lưu hành và sổ ghi danh thí chủ cúng dường"""
    @staticmethod
    def register_artifact(metadata, output_dir="catalog"):
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs("synapses", exist_ok=True)

        artifact_id = len(CatalogManager.load_catalog().get("items", [])) + 1
        meta_filename = os.path.join(output_dir, f"artifact_{artifact_id}.json")
        svg_filename = os.path.join(output_dir, f"artifact_{artifact_id}.svg")

        # Lưu ảnh SVG độc lập
        with open(svg_filename, "w", encoding="utf-8") as f:
            f.write(metadata["image_data"])

        # Lưu metadata JSON
        clean_meta = dict(metadata)
        clean_meta["image_url"] = f"https://raw.githubusercontent.com/100048777766367/nexus-forge/main/{svg_filename}"
        with open(meta_filename, "w", encoding="utf-8") as f:
            json.dump(clean_meta, f, indent=4, ensure_ascii=False)

        # Cập nhật catalog.json
        cat = CatalogManager.load_catalog()
        cat["items"].append({
            "id": artifact_id,
            "name": clean_meta["name"],
            "tier_price_usd": clean_meta["price_usd"],
            "raffle_ticket_id": clean_meta["raffle_entitlement"]["ticket_id"],
            "meta_uri": meta_filename,
            "status": "Available_For_Patronage"
        })
        cat["total_minted"] = len(cat["items"])
        
        with open(CATALOG_FILE, "w", encoding="utf-8") as f:
            json.dump(cat, f, indent=4, ensure_ascii=False)

        print(f"🔨 [ĐÚC THÀNH CÔNG] Vật phẩm #{artifact_id} ({clean_meta['name']}) đã lên kệ! Giá: ${clean_meta['price_usd']:.2f}")

    @staticmethod
    def load_catalog():
        if os.path.exists(CATALOG_FILE):
            try:
                with open(CATALOG_FILE, "r", encoding="utf-8") as f: return json.load(f)
            except Exception: pass
        return {"items": [], "total_minted": 0, "vault_network": "Base"}

    @staticmethod
    def record_patron(wallet_address, artifact_id, tx_hash, amount_usd):
        os.makedirs("synapses", exist_ok=True)
        patrons = []
        if os.path.exists(PATRON_FILE):
            try:
                with open(PATRON_FILE, "r", encoding="utf-8") as f: patrons = json.load(f)
            except Exception: pass

        record = {
            "patron_wallet": wallet_address,
            "artifact_id": artifact_id,
            "tx_hash": tx_hash,
            "amount_usd": amount_usd,
            "consecration": "Alms_Merit_Recorded"
        }
        patrons.append(record)
        with open(PATRON_FILE, "w", encoding="utf-8") as f:
            json.dump(patrons, f, indent=4, ensure_ascii=False)
        print(f"🙏 [CÔNG ĐỨC KHẮC BIA] Thí chủ {wallet_address[:10]}... đã cúng dường ${amount_usd:.2f}!")
