from pathlib import Path


def test_tmp_file_read(sample_text: Path) -> None:
    lines: list[str] = sample_text.read_text(encoding="utf-8").splitlines()
    assert lines == ["line1", "line2", "line3"]
