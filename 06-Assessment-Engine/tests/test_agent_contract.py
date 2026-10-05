from pathlib import Path

import yaml


def test_ai_discovery_agent_and_browser_handoff_exist():
    kit_root = Path(__file__).resolve().parents[2]
    agent_path = (
        kit_root
        / "05-Copilot-Workspace"
        / ".github"
        / "agents"
        / "fabric-adoption-discovery.agent.md"
    )
    content = agent_path.read_text(encoding="utf-8")
    _, frontmatter, body = content.split("---", maxsplit=2)
    metadata = yaml.safe_load(frontmatter)
    html = (
        kit_root
        / "03-Prototype-and-Testing"
        / "Fabric_Migration_Readiness_Assistant.html"
    ).read_text(encoding="utf-8")

    assert metadata["name"] == "Fabric Adoption Discovery"
    assert "microsoft-learn/*" in metadata["tools"]
    assert "adaptive conversation" in body
    assert 'id="startAiDiscoveryBtn"' in html
    assert 'readiness === null ? "N/A"' in html