import requests
import os
from pathlib import Path
import time

# Paper list from both forum posts
papers = [
    # Week: Jan 19-25, 2026
    {
        "title": "Agentic Reasoning for Large Language Models",
        "arxiv_id": "2601.12538",
        "week": "2026-01-19_25"
    },
    {
        "title": "Agentic-R - Learning to Retrieve for Agentic Search",
        "arxiv_id": "2601.11888",
        "week": "2026-01-19_25"
    },
    {
        "title": "STEM - Scaling Transformers with Embedding Modules",
        "arxiv_id": "2601.10639",
        "week": "2026-01-19_25"
    },
    {
        "title": "Agentic Operator Generation for ML ASICs",
        "arxiv_id": "2512.10977",
        "week": "2026-01-19_25"
    },
    {
        "title": "EvoCUA - Evolving Computer Use Agents via Learning from Scalable Synthetic Experience",
        "arxiv_id": "2601.15876",
        "week": "2026-01-19_25"
    },
    {
        "title": "The Dawn of Agentic EDA - A Survey of Autonomous Digital Chip Design",
        "arxiv_id": "2512.23189",
        "week": "2026-01-19_25"
    },
    {
        "title": "Confucius Code Agent - Scalable Agent Scaffolding for Real-World Codebases",
        "arxiv_id": "2512.10398",
        "week": "2026-01-19_25"
    },
    {
        "title": "UFT - Unifying Supervised and Reinforcement Fine-Tuning",
        "arxiv_id": "2505.16984",
        "week": "2026-01-19_25"
    },
    {
        "title": "UniversalRAG - Retrieval-Augmented Generation over Corpora of Diverse Modalities and Granularities",
        "arxiv_id": "2504.20734",
        "week": "2026-01-19_25"
    },
    {
        "title": "A Large-Scale Study on the Development and Issues of Multi-Agent AI Systems",
        "arxiv_id": "2601.07136",
        "week": "2026-01-19_25"
    },
    
    # Week: Dec 29, 2025 - Jan 4, 2026
    {
        "title": "mHC - Manifold-Constrained Hyper-Connections",
        "arxiv_id": "2512.24880",
        "week": "2025-12-29_2026-01-04"
    },
    {
        "title": "SCP - Accelerating Discovery with a Global Web of Autonomous Scientific Agents",
        "arxiv_id": "2512.24189",
        "week": "2025-12-29_2026-01-04"
    },
    {
        "title": "Evaluating Parameter Efficient Methods for RLVR",
        "arxiv_id": "2512.23165",
        "week": "2025-12-29_2026-01-04"
    },
    {
        "title": "Step-DeepResearch Technical Report",
        "arxiv_id": "2512.20491",
        "week": "2025-12-29_2026-01-04"
    },
    {
        "title": "Attention Is Not What You Need",
        "arxiv_id": "2512.19428",
        "week": "2025-12-29_2026-01-04"
    },
    {
        "title": "One Tool Is Enough - Reinforcement Learning for Repository-Level LLM Agents",
        "arxiv_id": "2512.20957",
        "week": "2025-12-29_2026-01-04"
    },
    {
        "title": "Sophia - A Persistent Agent Framework of Artificial Life",
        "arxiv_id": "2512.18202",
        "week": "2025-12-29_2026-01-04"
    },
    {
        "title": "VL-JEPA - Joint Embedding Predictive Architecture for Vision-Language",
        "arxiv_id": "2512.10942",
        "week": "2025-12-29_2026-01-04"
    },
    {
        "title": "Universal Reasoning Model",
        "arxiv_id": "2512.14693",
        "week": "2025-12-29_2026-01-04"
    },
    {
        "title": "Professional Software Developers Don't Vibe They Control - AI Agent Use for Coding in 2025",
        "arxiv_id": "2512.14012",
        "week": "2025-12-29_2026-01-04"
    },
]

def sanitize_filename(filename):
    """Remove or replace characters that are invalid in Windows filenames"""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '-')
    return filename

def download_paper(arxiv_id, title, week, base_dir):
    """Download a paper from arXiv"""
    # Create week directory
    week_dir = Path(base_dir) / week
    week_dir.mkdir(parents=True, exist_ok=True)
    
    # Sanitize title for filename
    safe_title = sanitize_filename(title)
    filename = f"{safe_title}.pdf"
    filepath = week_dir / filename
    
    # Skip if already downloaded
    if filepath.exists():
        print(f"[OK] Already exists: {filename}")
        return True
    
    # Download from arXiv
    url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    print(f"Downloading: {title}")
    print(f"  URL: {url}")
    
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        print(f"[OK] Downloaded: {filename}")
        return True
        
    except Exception as e:
        print(f"[ERROR] Error downloading {title}: {e}")
        return False

def main():
    base_dir = Path(__file__).parent
    print(f"Download directory: {base_dir}")
    print(f"Total papers to download: {len(papers)}\n")
    
    success_count = 0
    fail_count = 0
    
    for i, paper in enumerate(papers, 1):
        print(f"\n[{i}/{len(papers)}] Processing...")
        if download_paper(paper['arxiv_id'], paper['title'], paper['week'], base_dir):
            success_count += 1
        else:
            fail_count += 1
        
        # Be nice to arXiv servers
        if i < len(papers):
            time.sleep(2)
    
    print(f"\n{'='*60}")
    print(f"Download complete!")
    print(f"Success: {success_count}")
    print(f"Failed: {fail_count}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
