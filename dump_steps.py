import json

log_path = "/Users/satoseiya/.gemini/antigravity/brain/eb16613e-8eef-4f7c-b431-7b4ece2b7614/.system_generated/logs/transcript.jsonl"

steps_to_dump = [540, 544, 558, 568, 576, 580, 588, 596, 614, 616, 622, 632, 640, 646, 652, 660, 666, 676, 682, 768, 790, 860, 893]

out_lines = []

with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line)
            step_idx = data.get("step_index")
            if step_idx in steps_to_dump:
                out_lines.append(f"=== STEP {step_idx} ({data.get('type')}) ===")
                if "tool_calls" in data:
                    for tc in data["tool_calls"]:
                        out_lines.append(f"  Tool: {tc.get('name')}")
                        args = tc.get("args", {})
                        if isinstance(args, str):
                            try:
                                args = json.loads(args)
                            except Exception:
                                pass
                        if isinstance(args, dict):
                            for k, v in args.items():
                                if k in ["CodeContent", "ReplacementContent", "TargetContent", "ReplacementChunks"]:
                                    out_lines.append(f"    {k} (len={len(str(v))}):")
                                    # 改行などを綺麗に出力するためにreprではなくそのまま出力
                                    out_lines.append(str(v))
                                else:
                                    out_lines.append(f"    {k}: {v}")
                out_lines.append("\n" + "="*80 + "\n")
        except Exception as e:
            pass

with open("/Users/satoseiya/.gemini/antigravity/brain/6297852c-fab6-435c-afc0-21ccc71403c0/scratch/dumped_steps.txt", "w", encoding="utf-8") as out:
    out.write("\n".join(out_lines))
print("Dumped steps to scratch/dumped_steps.txt")
