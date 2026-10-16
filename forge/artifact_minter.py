import json
from forge.svg_generator import GenerativeSVGArt
from forge.proof_attestation import ProofAttestation

TIER_CONFIG = {
    "tier_1": {
        "name": "Hạt Mầm Nhân Duyên (Causal Seed)",
        "price_usd": 0.20,
        "tickets_granted": 1,
        "palette": "sacred"
    },
    "tier_2": {
        "name": "Mảnh Toàn Ảnh Indra (Indra Fragment)",
        "price_usd": 0.50,
        "tickets_granted": 3,
        "palette": "electric"
    },
    "tier_3": {
        "name": "Kỷ Vật Thập Tứ Vô Úy (Sovereign Relic)",
        "price_usd": 1.00,
        "tickets_granted": 10,
        "palette": "sacred"
    }
}

class ArtifactMinter:
    """Đóng gói vật phẩm theo chuẩn OpenSea / EIP-721 / EIP-1155 Metadata"""
    @staticmethod
    def mint(artifact_id, tier_key, epoch, decision, coherence_r, wisdom_text, repo_origin):
        tier = TIER_CONFIG.get(tier_key, TIER_CONFIG["tier_1"])
        
        # Sinh tranh SVG
        svg_art = GenerativeSVGArt.render(artifact_id, epoch, decision, coherence_r, tier["palette"])
        
        # Ký chứng thực mật mã
        proof = ProofAttestation.generate_proof(artifact_id, epoch, decision, wisdom_text, repo_origin)
        
        # Mã vé số nhân quả
        raffle_ticket_id = f"TICKET-EP{epoch}-A{artifact_id}-{proof['signature'][:8]}"

        metadata = {
            "name": f"{tier['name']} #{artifact_id}",
            "description": f"Kỷ vật số chứng thực công đức được đúc tự động bởi Nexus-Forge thế hệ #{epoch}. Giá trị tượng trưng: ${tier['price_usd']:.2f} USD như một hành vi cúng dường hợp pháp nuôi sống hệ sinh thái.",
            "price_usd": tier["price_usd"],
            "currency": "USDC_on_Base",
            "image_data": svg_art,
            "attributes": [
                {"trait_type": "Generation Epoch", "value": epoch},
                {"trait_type": "Tier", "value": tier["name"]},
                {"trait_type": "Decision Phase", "value": decision},
                {"trait_type": "Kuramoto Coherence", "value": f"{coherence_r * 100:.2f}%"},
                {"trait_type": "Wisdom Root", "value": wisdom_text[:60] + "..."},
                {"trait_type": "Raffle Tickets Granted", "value": tier["tickets_granted"]},
                {"trait_type": "Raffle Ticket ID", "value": raffle_ticket_id}
            ],
            "cryptographic_proof": proof,
            "raffle_entitlement": {
                "ticket_id": raffle_ticket_id,
                "ticket_count": tier["tickets_granted"],
                "status": "Eligible_For_Nexus_Lottery"
            }
        }
        return metadata, svg_art
