import zipfile, os, datetime
from xml.sax.saxutils import escape

slides = [
("Nuriy", ["Verification Infrastructure for Jewelry Sustainability","What LEED did for buildings, Nuriy does for jewelry","Confidential — February 2026"]),
("Every Jewelry Brand Faces a Compliance Crisis",[
"REGULATORY MANDATE","• EU CSDDD requires supply chain verification by 2027","• Brands must prove no child labor or face fines and market restrictions","• Modern Slavery Act (UK) and pending US legislation create legal obligations",
"TRUST GAP","• 68% of consumers distrust sustainability claims","• Brands cannot differentiate genuine ethics from greenwashing","• 1M+ children exploited in jewelry supply chains",
"INFRASTRUCTURE VOID","• No independent product-level verification system exists","• Brands will not build this themselves","• Certification bodies use slow, expensive human auditors",
"This is not a 'nice to have' — it's mandatory compliance infrastructure"]),
("A $300B+ Industry Requires Third-Party Verification",[
"• Global Jewelry Industry: $300B+ (4-6% CAGR)","• EU CSDDD Compliance Market: Multi-billion (emerging, regulatory-driven)","• Supply Chain Transparency Software: $8.5B (12% CAGR)","• Ethical Jewelry Market: $22B (8-10% CAGR)",
"This is compliance-driven, non-discretionary B2B software — brands buy because lawyers and regulators require it, not sentiment",
"Starting in jewelry, expanding into fashion, cosmetics, and food"]),
("What LEED Did for Buildings, Nuriy Does for Jewelry",[
"LEFT SIDE — LEED Model: 1) Buildings earn certification 2) Display LEED label 3) Tenants demand it 4) Becomes industry standard",
"RIGHT SIDE — NURIY Model: 1) Products earn Nuriy Score 2) Brands display verification label 3) Consumers demand it 4) Becomes industry standard",
"• Scoring Engine: 0-100 transparency score (durability, materials, labor, certifications, environmental impact)","• Certification Standard: Brands seek, earn, license, and display Nuriy Score","• Infrastructure Layer: APIs, audit ledger, cryptographic integrity",
"Nuriy owns the infrastructure underneath the standard"]),
("Four-Layer Verification Stack",[
"Layer 1 (Foundation): NURIY SCORE METHODOLOGY — Structured scoring framework | Patent-pending",
"Layer 2: AUDIT SYNTHESIS PIPELINE — AI reasoning + evidence gathering → consistent audit outputs",
"Layer 3: EVIDENCE CLASSIFICATION SYSTEM — Tier A: Audited/Verified | Tier B: Self-Reported | Tier C: Missing/Unverified",
"Layer 4 (Top): AUDIT INTEGRITY LAYER — Cryptographic hashing | Tamper-proof permanent records",
"Data Moat: 752+ products scored — every audit improves accuracy"]),
("Mandatory Compliance Creates Non-Discretionary Demand",[
"2027: EU CSDDD — Supply chain due diligence required | Brands must verify no child labor",
"2024-Present: Modern Slavery Act (UK) — Enterprise buyers must verify and disclose supply chain practices",
"2026-2027: US Legislation (Pending) — Supply chain transparency obligations for enterprise buyers",
"Ongoing: EU Taxonomy Regulation — Auditable ESG claims required for public companies and partners",
"Brands will not buy Nuriy because they want to feel good — they buy it because their lawyers, procurement teams, and regulators require it"]),
("Compliance-Driven B2B SaaS + Certification Licensing",[
"1. B2B SaaS SUBSCRIPTIONS — $299-$999/month | API access, white-label verification | Primary revenue driver",
"2. ENTERPRISE CONTRACTS — $50K+ annual | Large retailers, ESG consultancies, compliance buyers",
"3. CERTIFICATION LICENSING — Medium-term | Brands pay to earn and display Nuriy Score label",
"4. API TRANSACTION FEES — $0.10 per verification at volume","5. Consumer Subscriptions (Secondary) — $9.99/month | Freemium model creates demand signal",
"Basic ($299) | Standard ($599) | Pro ($999) | Enterprise (Custom)"]),
("Three-Phase Playbook: Calibration → Signal → Standard",[
"PHASE 1: CALIBRATION (Current - Through March) — Stabilize scoring engine; 12 design partner jewelers; 13,588 email signups (zero paid acquisition); Infrastructure hardening",
"PHASE 2: ACTIVATION (April Onward) — Launch public URL-in → score-out tool; Close first 3-5 paying B2B customers; Partner with certification bodies; Infrastructure-first narrative",
"PHASE 3: STANDARD (H2 2026) — Chrome extension: score any jewelry URL; Enterprise sales to compliance buyers; Certification label program launch; Category expansion exploration",
"13,588 signups create bottom-up B2B demand: 'Our customers are asking for Nuriy Scores — how do we get certified?'"]),
("Infrastructure Ready, Demand Validated (Zero Paid Acquisition)",[
"13,588 EMAIL SIGNUPS — Organic demand signal before full launch","752+ PRODUCTS SCORED — Data moat accumulating — every audit improves accuracy",
"12 VERIFIED JEWELERS LIVE — Design partners shaping API product-market fit","7,877 INSTAGRAM FOLLOWERS — Community building validation",
"We didn't manufacture demand. We built infrastructure and demand found us.","April 1: Public URL-in → score-out tool launch"]),
("No Product-Level Verification Infrastructure Exists",[
"WHAT EXISTS: ❌ Brand-level ratings (Good On You) — not product-specific; ❌ Blockchain requiring brand cooperation (Provenance, TrustChain); ❌ Human auditor certifications (SCS, RJC) — slow, expensive, not scalable; ❌ Horizontal ESG platforms (EcoVadis) — not jewelry-specific; ❌ Single-asset tracking (Everledger) — diamonds only",
"WHAT NURIY DOES: ✓ Product-level URL-in → score-out; ✓ Works without brand cooperation; ✓ AI-powered, scalable infrastructure; ✓ Jewelry-specific methodology (patent-pending); ✓ Positioned to become certification standard",
"Nobody has built product-level, AI-powered scoring infrastructure specifically for jewelry that can become an industry certification standard"]),
("Supply Chain Verification Infrastructure — Starting in Jewelry",[
"NOW: JEWELRY — Child labor | Conflict minerals | Greenwashing | CSDDD compliance","2027: FASHION — Labor conditions | Synthetic materials | EU textile regulation",
"2027-2028: COSMETICS — Ingredient sourcing | Cruelty-free verification | Clean beauty claims","2028+: FOOD — Traceability | Organic/fair trade | Food safety",
"The same macro shift is happening across every category. Gen Z and Millennials demand proof. Nuriy builds the infrastructure layer the entire shift requires.","Jewelry is the beachhead. The infrastructure is the business."]),
("Vertical Compliance Infrastructure with Proven Models",[
"VITAL4 | AML & Financial Crime Intelligence — For jewelry supply chains, what Vital4 is for financial crime — structures complex risk data into actionable compliance intelligence",
"VISALAW.AI | Immigration Law AI — Vertical AI that standardizes, scores, and operationalizes complex evidence in a specific domain",
"FINQUERY | Lease Accounting Compliance — Turns dense technical documentation into standardized, auditable numbers — lease obligations for them, sustainability scores for us",
"Each became the system of record for high-stakes compliance in their vertical"]),
("Systems Operator with Domain Expertise",[
"AALIYA [Last Name] — Founder & CEO","• 15+ years in tech and operations","• Program Manager at Wellstar","• Former Harvard Med School, large tech companies",
"• Built and exited previous business (10 years)","• Systems thinker: 'I help people get things done'",
"Domain Expertise: Mother sold jewelry — personal connection to industry; Deep supply chain and verification knowledge; Patent-pending scoring methodology architect"]),
("MRR Growth Through B2B SaaS, Not Marketplace Transactions",[
"PHASE 1 (Jan-Feb): $3K-$4K MRR — 12 jewelers | Design partners converting | Infrastructure complete",
"PHASE 2 (Mar-May): $10K-$15K MRR — 20 jewelers | First paying B2B customers | API pilots",
"PHASE 3 (Jun-Dec): $40K-$60K MRR — 50 jewelers | Chrome extension | Enterprise contracts",
"• Monthly Burn: $5K","• GMV Target 2026: $750K","• Primary Revenue: B2B SaaS subscriptions",
"Path to profitability through recurring B2B revenue, not marketplace commissions"]),
("$500K to Activate the Infrastructure",[
"1. AUDIT INTEGRITY LAYER ($150K) — Complete cryptographic hashing for enterprise-grade verification",
"2. API BUILD-OUT & B2B SALES ($250K) — Close first 3-5 paying customers | Integration tooling | Sales enablement",
"3. CHROME EXTENSION LAUNCH ($100K) — Extend scoring beyond marketplace to any jewelry URL on the web",
"Use of funds timeline: Q1-Q2 2026","Capital doesn't buy time — it buys speed. The infrastructure works. This funds activation without triage.","Valuation: $2.5M pre-money","Contact: [Email] | nuriy.com/invest"])
]

W=12192000; H=6858000

def sp(id_, name, x,y,cx,cy, text, sz=2400, bold='0', color='F1F5F9'):
    paras=''
    for i,line in enumerate(text.split('\n')):
        paras += f'<a:p><a:r><a:rPr lang="en-US" sz="{sz}" b="{bold}"><a:solidFill><a:srgbClr val="{color}"/></a:solidFill></a:rPr><a:t>{escape(line)}</a:t></a:r><a:endParaRPr lang="en-US"/></a:p>'
    return f'''<p:sp><p:nvSpPr><p:cNvPr id="{id_}" name="{name}"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr><p:spPr><a:xfrm><a:off x="{x}" y="{y}"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:noFill/></p:spPr><p:txBody><a:bodyPr wrap="square"/><a:lstStyle/>{paras}</p:txBody></p:sp>'''

def slide_xml(title, lines, idx):
    shapes=[sp(2,'Title',500000,300000,11200000,900000,title,sz=3600,bold='1',color='38BDF8')]
    y=1400000
    sid=3
    for ln in lines:
        shapes.append(sp(sid,f'Text{sid}',700000,y,10800000,420000,ln,sz=1700,color='F1F5F9'))
        y += 380000
        sid+=1
    shapes.append(sp(99,'Footer',500000,6400000,11200000,250000,f'Nuriy — Confidential    {idx}',sz=1200,color='94A3B8'))
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"><p:cSld><p:bg><p:bgPr><a:solidFill><a:srgbClr val="0F172A"/></a:solidFill></p:bgPr></p:bg><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>{''.join(shapes)}</p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:sld>'''

os.makedirs('out',exist_ok=True)
pptx_path='out/Nuriy_Investor_Deck.pptx'
with zipfile.ZipFile(pptx_path,'w',zipfile.ZIP_DEFLATED) as z:
    z.writestr('[Content_Types].xml',f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>{''.join([f'<Override PartName="/ppt/slides/slide{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>' for i in range(1,16)])}</Types>''')
    z.writestr('_rels/.rels','''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/></Relationships>''')
    z.writestr('ppt/presentation.xml',f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentation xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"><p:sldIdLst>{''.join([f'<p:sldId id="{255+i}" r:id="rId{i}"/>' for i in range(1,16)])}</p:sldIdLst><p:sldSz cx="{W}" cy="{H}" type="screen16x9"/><p:notesSz cx="6858000" cy="9144000"/></p:presentation>''')
    z.writestr('ppt/_rels/presentation.xml.rels',f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">{''.join([f'<Relationship Id="rId{i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide{i}.xml"/>' for i in range(1,16)])}</Relationships>''')
    for i,(title,lines) in enumerate(slides, start=1):
        z.writestr(f'ppt/slides/slide{i}.xml',slide_xml(title,lines,i))
print('wrote',pptx_path)

# very simple PDF
pdf='out/Nuriy_Investor_Deck.pdf'
objs=[]
def add_obj(data): objs.append(data); return len(objs)
font_id=add_obj(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
pages=[]
for i,(title,lines) in enumerate(slides, start=1):
    content=[b"0.06 0.09 0.16 rg 0 0 792 612 re f", b"BT /F1 24 Tf 0.22 0.74 0.97 rg 40 560 Td ("+escape(title).encode('latin-1','replace')+b") Tj ET"]
    y=530
    for ln in lines:
        txt=ln.replace('—','-').replace('→','->').replace('✓','+').replace('❌','x').replace('“','"').replace('”','"').replace('’',"'")
        content.append(f"BT /F1 11 Tf 0.95 0.96 0.98 rg 40 {y} Td ({txt[:140]}) Tj ET".encode('latin-1','replace'))
        y-=18
        if y<40: break
    content.append(f"BT /F1 9 Tf 0.58 0.64 0.72 rg 600 20 Td (Nuriy - Confidential {i}) Tj ET".encode())
    stream=b"\n".join(content)
    cid=add_obj(f"<< /Length {len(stream)} >>\nstream\n".encode()+stream+b"\nendstream")
    pid=add_obj(f"<< /Type /Page /Parent 0 0 R /MediaBox [0 0 792 612] /Resources << /Font << /F1 {font_id} 0 R >> >> /Contents {cid} 0 R >>".encode())
    pages.append(pid)
kids=' '.join([f'{p} 0 R' for p in pages])
pages_id=add_obj(f"<< /Type /Pages /Kids [{kids}] /Count {len(pages)} >>".encode())
for p in pages:
    objs[p-1]=objs[p-1].replace(b'/Parent 0 0 R',f'/Parent {pages_id} 0 R'.encode())
catalog_id=add_obj(f"<< /Type /Catalog /Pages {pages_id} 0 R >>".encode())

with open(pdf,'wb') as f:
    f.write(b'%PDF-1.4\n')
    xref=[0]
    for i,o in enumerate(objs, start=1):
        xref.append(f.tell()); f.write(f"{i} 0 obj\n".encode()); f.write(o); f.write(b"\nendobj\n")
    xref_pos=f.tell(); f.write(f"xref\n0 {len(objs)+1}\n".encode()); f.write(b"0000000000 65535 f \n")
    for off in xref[1:]: f.write(f"{off:010d} 00000 n \n".encode())
    f.write(f"trailer\n<< /Size {len(objs)+1} /Root {catalog_id} 0 R >>\nstartxref\n{xref_pos}\n%%EOF".encode())
print('wrote',pdf)
