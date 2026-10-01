#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Terlik Yönü Denetim Kurumu — saha yazılımı.

Terlik gerçekten dönmez. Yazılım döner. Bu yeter.
"""

from __future__ import annotations

import argparse
import random
import sys
from datetime import datetime

YONLER = (
    "kapiya",
    "duvara",
    "birbirine",
    "buzdolabina",
    "televizyonun utangac tarafina",
    "komsunun terligine",
    "belirsiz bir felsefeye",
)

UYGUN = {"kapiya"}

IC_CEKISLER = (
    "Kurum iç çekti. İç çekiş tutanağa işlendi.",
    "Sekreter iç çekti, sonra bunun da yönetmelikte olduğunu hatırladı.",
    "İç çekiş Dairesi mesaiye kaldı. Fazla mesai çay ile ödenir.",
    "Cezası yok. Cezası olmaması da tutanak.",
)


def karar(yon: str) -> str:
    if yon in UYGUN:
        return "uygun"
    if yon == "birbirine":
        return "romantik ama usulsüz"
    if "felsefe" in yon:
        return "kapsam dışı, felsefe şubesi kapalı"
    return "kuşkulu"


def tutanak_no() -> str:
    bugun = datetime.now().strftime("%Y%m%d")
    return f"TYDK-{bugun}-{random.randint(10, 99)}"


def denetle(sol: str, sag: str, oda: str) -> str:
    sol_k = karar(sol)
    sag_k = karar(sag)
    satirlar = [
        f"TUTANAK NO: {tutanak_no()}",
        f"Tarih: {datetime.now():%d.%m.%Y %H:%M}",
        f"Oda: {oda}",
        f"Sol terlik: {sol} ({sol_k})",
        f"Sağ terlik: {sag} ({sag_k})",
        "-",
    ]
    if sol_k == "uygun" and sag_k == "uygun":
        satirlar.append("Karar: Çift usulüne uygun. Kurum sıkıldı, yine de onayladı.")
    elif sol == sag and sol not in UYGUN:
        satirlar.append("Karar: İkisi de aynı yanlışa bakıyor. Bu bir ekip ruhu değil, organize ihlal.")
    else:
        satirlar.append("Karar: Kısmi ihtar. Terlikler 90 derece döndürülecek, döndüren kişi tutanakta 'gönüllü' yazılacak.")
    satirlar.append(random.choice(IC_CEKISLER))
    satirlar.append("Mühür: basıldı (mürekkep bitti, basılmış sayılır).")
    return "\n".join(satirlar)


def rastgele_cift() -> tuple[str, str]:
    return random.choice(YONLER), random.choice(YONLER)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Terlik Yönü Denetim Kurumu saha yazılımı"
    )
    p.add_argument("--cift", nargs=2, metavar=("SOL", "SAG"), help="sol ve sağ terlik yönü")
    p.add_argument("--oda", default="antre")
    p.add_argument("--rastgele", type=int, default=0, help="kaç rastgele denetim")
    p.add_argument("--tutanak", action="store_true", help="her zaman tutanak bas")
    args = p.parse_args(argv)

    turlar = args.rastgele or 1
    for i in range(turlar):
        if args.cift and i == 0:
            sol, sag = args.cift
        else:
            sol, sag = rastgele_cift()
        print(denetle(sol, sag, args.oda))
        if i != turlar - 1:
            print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
