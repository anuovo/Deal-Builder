import streamlit as st
from streamlit.components.v1 import html


st.set_page_config(page_title="Suppliers by Commodity", layout="wide")

st.markdown(
    """
    <style>
    [data-testid="stHeader"], [data-testid="stToolbar"] {
        display: none;
    }

    .stApp {
        background: #f6f8fb;
    }

    .block-container {
        max-width: 1600px;
        padding-top: 0.35rem;
        padding-bottom: 0.35rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


APP_HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Suppliers by Commodity</title>
<style>
:root{
  --bg:#f6f8fb;
  --panel:#ffffff;
  --ink:#172033;
  --muted:#7e8ea8;
  --line:#e3eaf4;
  --green:#1aa64a;
  --olive:#7d8d1f;
  --red:#ff564d;
  --blue:#2d5bdf;
  --blue-soft:#edf3ff;
  --flash:#fff4bf;
  --shadow:0 10px 30px rgba(15, 23, 42, .06);
}
*{box-sizing:border-box}
body{
  margin:0;
  background:var(--bg);
  color:var(--ink);
  font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",system-ui,sans-serif;
}
.shell{
  max-width:1560px;
  margin:0 auto;
  background:var(--panel);
  border:1px solid var(--line);
  border-radius:22px;
  box-shadow:var(--shadow);
  padding:20px 18px 24px;
  min-height:1080px;
  position:relative;
  z-index:2;
  isolation:isolate;
}
.board-top{
  display:flex;
  align-items:flex-start;
  gap:18px;
  margin-bottom:18px;
}
.logo-box{
  width:58px;
  height:58px;
  border-radius:14px;
  background:#23252e;
  display:flex;
  align-items:center;
  justify-content:center;
  flex:0 0 auto;
}
.logo-mark{
  position:relative;
  width:34px;
  height:38px;
}
.logo-mark .g{
  position:absolute;
  inset:auto 0 0 0;
  color:#d7e521;
  font-size:32px;
  font-weight:900;
  line-height:1;
}
.logo-mark .leaf-left,
.logo-mark .leaf-right{
  position:absolute;
  top:0;
  width:13px;
  height:18px;
  border-radius:12px 12px 2px 12px;
}
.logo-mark .leaf-left{
  left:2px;
  background:#ffbd47;
  transform:rotate(-24deg);
}
.logo-mark .leaf-right{
  right:2px;
  background:#9fcb29;
  transform:rotate(22deg);
}
.board-head{
  flex:1;
}
.eyebrow{
  margin:0;
  color:#7a8ba5;
  font-size:16px;
  font-weight:900;
  letter-spacing:.06em;
  text-transform:uppercase;
}
.board-sub{
  margin-top:6px;
  color:#56657d;
  font-size:12px;
}
.board-grid{
  display:grid;
  grid-template-columns:repeat(3,minmax(0,1fr));
  gap:14px;
  align-items:start;
  position:relative;
  z-index:4;
}
.shell.drawer-open{
  padding-bottom:380px;
}
.shell.drawer-open::after{
  content:"";
  position:fixed;
  inset:0;
  background:rgba(15,23,42,.18);
  pointer-events:none;
  z-index:1;
}
.board-grid.workspace-open .commodity-card.inactive{
  opacity:.45;
  transform:scale(.985);
  filter:saturate(.84);
}
.commodity-card{
  border:1px solid var(--line);
  border-radius:22px;
  overflow:hidden;
  background:#fff;
  cursor:pointer;
  transition:transform .18s ease,border-color .18s ease,box-shadow .18s ease,opacity .22s ease,filter .22s ease;
  position:relative;
}
.commodity-card:hover{
  transform:translateY(-2px);
  border-color:#cfd9ea;
  box-shadow:0 12px 26px rgba(15,23,42,.08);
}
.commodity-card.active{
  grid-column:1 / -1;
  border-color:#c5d8ff;
  box-shadow:0 0 0 3px rgba(45,91,223,.08),0 14px 28px rgba(15,23,42,.08);
  scroll-margin-top:12px;
  z-index:6;
}
.commodity-card.changed{
  box-shadow:0 0 0 3px rgba(255,220,99,.35),0 14px 28px rgba(15,23,42,.08);
}
.card-head{
  padding:16px 18px 14px;
  border-bottom:1px solid var(--line);
}
.card-head-row{
  display:flex;
  justify-content:space-between;
  align-items:flex-start;
  gap:12px;
}
.card-label{
  color:#7789a4;
  font-size:12px;
  font-weight:900;
  letter-spacing:.08em;
  text-transform:uppercase;
}
.active-pill{
  padding:6px 10px;
  border-radius:999px;
  background:#eef5ff;
  color:#1e4cd8;
  font-size:11px;
  font-weight:900;
  letter-spacing:.06em;
  text-transform:uppercase;
}
.locked-pill{
  padding:6px 10px;
  border-radius:999px;
  background:#edf8f1;
  color:#16763f;
  font-size:11px;
  font-weight:900;
  letter-spacing:.06em;
  text-transform:uppercase;
}
.card-header-row{
  margin-top:6px;
  display:flex;
  justify-content:space-between;
  align-items:flex-start;
  gap:12px;
}
.card-title{
  font-size:16px;
  font-weight:900;
  letter-spacing:-.02em;
}
.card-units{
  margin-left:6px;
  color:#70829c;
  font-weight:500;
  font-size:16px;
}
.card-meta{
  margin-top:6px;
  color:#93a3bb;
  font-size:12px;
  font-weight:500;
}
.card-summary{
  text-align:right;
  line-height:1.25;
}
.summary-line{
  font-size:14px;
  font-weight:500;
  color:#6f7f15;
}
.summary-line.red{
  color:var(--red);
}
.summary-line strong{
  font-weight:900;
}
.supplier-slot{
  display:grid;
  grid-template-columns:1fr auto;
  gap:10px;
  align-items:center;
  padding:16px 18px 15px;
  border-bottom:1px solid #edf2f8;
}
.supplier-slot:last-child{
  border-bottom:0;
}
.slot-label{
  color:#77831f;
  font-size:12px;
  font-weight:900;
  letter-spacing:.08em;
  text-transform:uppercase;
}
.slot-price{
  margin-top:6px;
  font-size:16px;
  font-weight:900;
  letter-spacing:-.02em;
  color:#2a2c35;
}
.slot-quote{
  margin-top:2px;
  color:#7184a2;
  font-size:14px;
}
.slot-quote strong{
  color:#1f2535;
  font-weight:900;
}
.slot-delta{
  margin-top:4px;
  font-size:14px;
}
.slot-delta.green{
  color:var(--green);
}
.slot-delta.red{
  color:var(--red);
}
.supplier-name{
  text-align:right;
  font-size:14px;
  color:#56657d;
}
.flash{
  display:inline-block;
  padding:0 .15em;
  border-radius:8px;
  animation:flashField 1.35s ease;
}
@keyframes flashField{
  0%{background:rgba(255,244,191,.95)}
  100%{background:transparent}
}
.workspace-drawer{
  position:fixed;
  left:16px;
  right:16px;
  top:calc(100vh - 380px);
  z-index:40;
  border:1px solid var(--line);
  border-radius:20px;
  overflow:hidden;
  background:#fff;
  box-shadow:0 22px 60px rgba(15,23,42,.16);
  transform:translateY(24px);
  opacity:0;
  pointer-events:none;
  transition:transform .24s ease, opacity .24s ease;
  z-index:50;
}
.workspace-drawer.open{
  transform:translateY(0);
  opacity:1;
  pointer-events:auto;
}
.workspace-chat{
  background:#fbfcff;
  display:flex;
  flex-direction:column;
  min-height:320px;
}
.workspace-top{
  display:flex;
  justify-content:space-between;
  align-items:flex-start;
  gap:12px;
  padding:16px 18px 10px;
  background:#fff;
}
.workspace-title{
  margin:0;
  font-size:16px;
  font-weight:900;
}
.close-btn{
  border:1px solid var(--line);
  background:#fff;
  color:#202a3a;
  border-radius:14px;
  padding:10px 14px;
  font-weight:800;
  cursor:pointer;
  flex:0 0 auto;
}
.thread{
  flex:1;
  padding:12px 18px 18px;
  overflow:auto;
  display:flex;
  flex-direction:column;
  gap:14px;
  min-height:0;
}
.quick-prompts{
  display:flex;
  gap:10px;
  flex-wrap:wrap;
  padding:14px 18px 0;
  background:#fff;
}
.quick-prompt{
  border:1px solid #d9e3f2;
  background:#f8fbff;
  color:#2a3f68;
  border-radius:999px;
  padding:9px 14px;
  font-size:12px;
  font-weight:800;
  cursor:pointer;
  transition:all .16s ease;
}
.quick-prompt:hover{
  border-color:#c1d3f6;
  background:#eef5ff;
}
.msg{
  max-width:88%;
  padding:14px 16px;
  border-radius:20px;
  line-height:1.5;
  font-size:14px;
  white-space:pre-wrap;
}
.msg.ai{
  background:#fff;
  border:1px solid var(--line);
  color:#33435d;
  border-top-left-radius:8px;
}
.msg.user{
  align-self:flex-end;
  background:#eaf1ff;
  color:#2348a6;
  border-top-right-radius:8px;
}
.composer-wrap{
  padding:14px 18px 18px;
  border-top:1px solid var(--line);
  background:#fff;
}
.composer-shell{
  display:flex;
  align-items:flex-end;
  gap:12px;
  border:1px solid var(--line);
  border-radius:18px;
  padding:10px 10px 10px 14px;
  background:#fff;
  max-width:760px;
}
.composer{
  flex:1;
  min-height:54px;
  max-height:54px;
  border:0;
  outline:none;
  resize:none;
  color:#33435d;
  font:inherit;
}
.send-btn{
  width:46px;
  height:46px;
  border:0;
  border-radius:16px;
  background:#19934d;
  color:#fff;
  cursor:pointer;
  display:flex;
  align-items:center;
  justify-content:center;
  box-shadow:0 10px 20px rgba(25,147,77,.22);
}
.send-btn svg{
  width:20px;
  height:20px;
}
.composer-note{
  margin-top:8px;
  color:#8b9ab1;
  font-size:12px;
}
.board-hint{
  margin-top:16px;
  padding:14px 16px;
  border:1px solid var(--line);
  border-radius:16px;
  background:linear-gradient(135deg,#f9fbff,#ffffff);
  color:#5b6b83;
  font-size:12px;
}
.build-deal-row{
  margin-top:16px;
  display:flex;
  justify-content:flex-start;
}
.build-deal-btn{
  border:0;
  border-radius:12px;
  background:#118847;
  color:#fff;
  font-size:12px;
  font-weight:900;
  padding:11px 18px;
  cursor:pointer;
  box-shadow:0 10px 20px rgba(17,136,71,.18);
}
.spot-shell{
  margin-top:22px;
  border:1px solid var(--line);
  border-radius:22px;
  background:#fff;
  box-shadow:var(--shadow);
  padding:18px;
  position:relative;
  z-index:2;
  cursor:pointer;
  transition:border-color .18s ease, box-shadow .18s ease, transform .18s ease;
}
.spot-shell.hidden{
  display:none;
}
.spot-shell:hover{
  border-color:#cfd9ea;
  box-shadow:0 12px 26px rgba(15,23,42,.08);
  transform:translateY(-1px);
}
.spot-shell.active{
  border-color:#c5d8ff;
  box-shadow:0 0 0 3px rgba(45,91,223,.08),0 14px 28px rgba(15,23,42,.08);
}
.spot-header{
  display:flex;
  justify-content:space-between;
  align-items:flex-start;
  gap:16px;
  margin-bottom:16px;
}
.spot-title{
  font-size:16px;
  font-weight:900;
}
.spot-title span{
  color:#64748b;
  font-weight:700;
}
.spot-pill{
  display:inline-block;
  margin-left:8px;
  padding:5px 10px;
  border-radius:999px;
  background:#edf7f1;
  color:#166534;
  font-size:11px;
  font-weight:900;
}
.spot-sub{
  margin-top:6px;
  color:#64748b;
  font-size:12px;
}
.spot-stats{
  margin-top:10px;
  display:flex;
  flex-wrap:wrap;
  gap:10px;
  color:#475569;
  font-size:12px;
}
.spot-stats strong{
  color:#0f172a;
}
.spot-optimized{
  padding:9px 14px;
  border:1px solid #b7e6c7;
  border-radius:12px;
  color:#118847;
  background:#eefcf4;
  font-size:12px;
  font-weight:900;
  white-space:nowrap;
}
.spot-header-right{
  display:flex;
  align-items:flex-start;
  gap:10px;
}
.spot-mode-toggle{
  display:flex;
  padding:4px;
  border:1px solid var(--line);
  border-radius:12px;
  background:#f8fafc;
}
.spot-mode-btn{
  border:0;
  background:transparent;
  color:#64748b;
  font-size:12px;
  font-weight:900;
  padding:8px 12px;
  border-radius:9px;
  cursor:pointer;
}
.spot-mode-btn.active{
  background:#eefcf4;
  color:#118847;
}
.spot-insight{
  display:grid;
  grid-template-columns:minmax(0,1fr) 172px 172px;
  border:1px solid var(--line);
  border-radius:18px;
  overflow:hidden;
}
.spot-insight-main{
  padding:18px 20px;
}
.spot-insight-label{
  color:#118847;
  font-size:12px;
  font-weight:900;
}
.spot-insight-head{
  margin-top:8px;
  font-size:16px;
  font-weight:900;
}
.spot-insight-sub{
  margin-top:8px;
  color:#475569;
  font-size:12px;
}
.spot-insight-sub .contract{
  color:#118847;
  font-weight:900;
}
.spot-insight-sub .spot{
  color:#2563eb;
  font-weight:900;
}
.spot-metric{
  border-left:1px solid var(--line);
  padding:18px 12px;
  text-align:center;
}
.spot-metric-k{
  color:#64748b;
  font-size:12px;
}
.spot-metric-v{
  margin-top:8px;
  color:#118847;
  font-size:16px;
  font-weight:900;
}
.spot-metric-sub{
  margin-top:4px;
  color:#16a34a;
  font-size:12px;
}
.spot-table{
  margin-top:16px;
  border:1px solid var(--line);
  border-radius:18px;
  overflow:hidden;
}
.spot-table table{
  width:100%;
  border-collapse:collapse;
}
.spot-table th{
  text-align:left;
  padding:12px 14px;
  background:#fbfdff;
  border-bottom:1px solid var(--line);
  color:#64748b;
  font-size:12px;
  letter-spacing:.04em;
}
.spot-table td{
  padding:14px;
  border-bottom:1px solid var(--line);
  vertical-align:top;
  font-size:14px;
}
.spot-table tr:last-child td{
  border-bottom:0;
}
.spot-item{
  font-size:14px;
  font-weight:900;
}
.spot-supplier{
  margin-top:4px;
  color:#64748b;
  font-size:12px;
}
.spot-request{
  font-weight:900;
}
.spot-bar{
  position:relative;
  width:300px;
  height:32px;
  border:1px solid #bfd7ff;
  border-radius:10px;
  overflow:hidden;
  display:flex;
  background:#f8fbff;
}
.spot-bar-contract{
  width:25%;
  display:flex;
  align-items:center;
  justify-content:center;
  background:#dff4e6;
  color:#118847;
  font-size:12px;
  font-weight:900;
}
.spot-bar-spot{
  width:75%;
  display:flex;
  align-items:center;
  justify-content:center;
  background:#edf4ff;
  color:#2563eb;
  font-size:12px;
  font-weight:900;
}
.spot-range{
  position:absolute;
  inset:0;
  width:100%;
  height:100%;
  opacity:0;
  cursor:ew-resize;
}
.spot-handle{
  position:absolute;
  top:2px;
  bottom:2px;
  width:4px;
  background:#fff;
  border:1px solid #93c5fd;
  border-radius:999px;
  transform:translateX(-50%);
  pointer-events:none;
  box-shadow:0 2px 8px rgba(37,99,235,.24);
}
.spot-handle::after{
  content:"";
  position:absolute;
  left:50%;
  top:50%;
  width:18px;
  height:18px;
  border-radius:50%;
  background:#fff;
  border:1px solid #93c5fd;
  transform:translate(-50%,-50%);
  box-shadow:0 2px 8px rgba(15,23,42,.12);
}
.spot-contract-copy{
  margin-top:8px;
  font-size:12px;
  color:#475569;
}
.spot-contract-copy .contract{
  color:#118847;
  font-weight:900;
}
.spot-contract-copy .spot{
  color:#2563eb;
  font-weight:900;
}
.spot-muted{
  margin-top:4px;
  color:#94a3b8;
  font-size:12px;
}
.spot-link{
  margin-top:6px;
  color:#1d4ed8;
  font-size:12px;
  font-weight:900;
  cursor:pointer;
}
.spot-contract-box{
  margin-top:8px;
  padding:10px 12px;
  border:1px solid var(--line);
  border-radius:12px;
  background:#f8fbff;
  color:#475569;
  font-size:12px;
  line-height:1.5;
}
.spot-contract-box strong{
  color:#0f172a;
}
.spot-contract-box.hidden{
  display:none;
}
.spot-pill-inline{
  display:inline-block;
  padding:6px 12px;
  border-radius:999px;
  border:1px solid #bfd7ff;
  background:#edf4ff;
  color:#2563eb;
  font-size:12px;
  font-weight:900;
}
.hidden{
  display:none !important;
}
.spot-price{
  font-size:14px;
  font-weight:900;
}
.spot-price-sub{
  margin-top:4px;
  color:#94a3b8;
  font-size:12px;
}
.spot-good{
  color:#118847;
  font-weight:900;
}
.spot-bad{
  color:#ef4444;
  font-weight:900;
}
.spot-usda-sub{
  margin-top:4px;
  color:#94a3b8;
  font-size:12px;
}
.spot-rec{
  display:flex;
  flex-wrap:wrap;
  gap:14px;
  padding:12px 14px;
  border-top:1px solid var(--line);
  color:#475569;
  font-size:12px;
}
.spot-rec .blue{
  color:#2563eb;
  font-weight:900;
}
.spot-rec .green{
  color:#118847;
  font-weight:900;
}
.spot-opportunity{
  margin-top:14px;
  display:flex;
  justify-content:space-between;
  align-items:center;
  gap:14px;
  padding:16px 18px;
  border:1px solid var(--line);
  border-radius:18px;
  background:linear-gradient(90deg,#f6fffa,#fff);
}
.spot-opp-title{
  font-size:14px;
  font-weight:900;
}
.spot-opp-sub{
  margin-top:4px;
  color:#118847;
  font-size:12px;
  font-weight:900;
}
.spot-action{
  border:0;
  border-radius:12px;
  background:#118847;
  color:#fff;
  font-size:12px;
  font-weight:900;
  padding:11px 22px;
}
.spot-system{
  margin-top:12px;
  padding:14px 18px;
  border:1px solid var(--line);
  border-radius:18px;
  color:#475569;
  font-size:12px;
}
.spot-system strong{
  color:#0f172a;
}
.spot-actions{
  margin-top:14px;
  display:flex;
  gap:10px;
}
.spot-btn-primary,.spot-btn-secondary{
  border:0;
  border-radius:12px;
  padding:11px 20px;
  font-size:12px;
  font-weight:900;
}
.spot-btn-primary{
  background:#118847;
  color:#fff;
}
.spot-btn-secondary{
  background:#eef2f7;
  color:#334155;
}
.spot-foot{
  margin-top:12px;
  text-align:center;
  color:#94a3b8;
  font-size:12px;
}
.green{color:var(--green)}
.red{color:var(--red)}
@media (max-width: 1280px){
  .board-grid{
    grid-template-columns:1fr;
  }
}
</style>
</head>
<body>
<div id="mainShell" class="shell">
  <div class="board-top">
    <div class="logo-box">
      <div class="logo-mark">
        <div class="leaf-left"></div>
        <div class="leaf-right"></div>
        <div class="g">G</div>
      </div>
    </div>
    <div class="board-head">
      <p class="eyebrow">Suppliers by Commodity</p>
      <div class="board-sub">Main Chat is the sourcing thread. Click a quote card to make it the active live object, then refine it with AI inline beneath the card.</div>
    </div>
  </div>

  <div id="boardGrid" class="board-grid"></div>

  <div class="board-hint">
    The selected quote card is the live procurement object. The workspace below it is only the conversational control layer for refining price, mix, units, terms, market position, and lock readiness.
  </div>

  <div class="build-deal-row">
    <button id="buildDealBtn" class="build-deal-btn" type="button">Build Deal</button>
  </div>

  <div id="spotShell" class="spot-shell hidden">
    <div class="spot-header">
      <div>
        <div class="spot-title">Deal Builder <span id="spotModePill" class="spot-pill">Contract-Aware</span></div>
        <div id="spotModeSub" class="spot-sub">AI optimized demand while respecting contract commitments.</div>
        <div class="spot-stats">
          <span>Items: <strong>3</strong></span>
          <span>|</span>
          <span>Requested: <strong>700 units</strong></span>
          <span>|</span>
          <span>Contract requested: <strong id="spotTopContract">125 units</strong></span>
          <span>|</span>
          <span>Spot: <strong id="spotTopSpot">600 units</strong></span>
        </div>
      </div>
      <div class="spot-header-right">
        <div class="spot-mode-toggle">
          <button id="spotModeContract" class="spot-mode-btn active" type="button">Contract Aware</button>
          <button id="spotModeMarket" class="spot-mode-btn" type="button">Spot Market</button>
        </div>
        <div class="spot-optimized">✓ OPTIMIZED</div>
      </div>
    </div>

    <div class="spot-insight">
      <div class="spot-insight-main">
        <div class="spot-insight-label">✦ Market Advantage</div>
        <div id="spotInsightHead" class="spot-insight-head">$169 below USDA across all items</div>
        <div class="spot-insight-sub"><span id="spotInsightContract" class="contract">125 units</span> requested from contract &nbsp;•&nbsp; <span id="spotInsightSpot" class="spot">600 units</span> via spot</div>
      </div>
      <div class="spot-metric">
        <div class="spot-metric-k">vs USDA Market</div>
        <div id="spotMetricUsda" class="spot-metric-v">$169 below</div>
        <div id="spotMetricUsdaPct" class="spot-metric-sub">(-12.8%)</div>
      </div>
      <div class="spot-metric">
        <div class="spot-metric-k">vs Supplier Avg.</div>
        <div id="spotMetricSupplier" class="spot-metric-v">$123 below</div>
        <div id="spotMetricSupplierPct" class="spot-metric-sub">(-7.4%)</div>
      </div>
    </div>

    <div class="spot-table">
      <table>
        <thead>
          <tr>
            <th>ITEM / SUPPLIER</th>
            <th>REQUESTED</th>
            <th>CONTRACT / SPOT</th>
            <th>PRICE / UNIT</th>
            <th>VS USDA</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              <div class="spot-item">Iceberg Lettuce</div>
              <div class="spot-supplier">Supplier A • Salinas, CA</div>
            </td>
            <td class="spot-request">500 units</td>
            <td>
              <div id="spotContractWrap">
                <div class="spot-bar">
                  <div id="spotBarContract" class="spot-bar-contract">25%</div>
                  <div id="spotBarSpot" class="spot-bar-spot">75%</div>
                  <div id="spotBarHandle" class="spot-handle" style="left:25%"></div>
                  <input id="spotSplitSlider" class="spot-range" type="range" min="0" max="200" step="25" value="125">
                </div>
                <div class="spot-contract-copy"><span id="spotContractText" class="contract">125 contract</span> &nbsp;|&nbsp; <span id="spotSpotText" class="spot">375 spot</span></div>
                <div class="spot-muted">Contracted volume: 100 cases</div>
                <div id="spotOverNote" class="spot-muted">Exceeds contracted volume; supplier may require spot pricing for additional units.</div>
                <div id="spotContractToggle" class="spot-link">Contract Info ▾</div>
                <div id="spotContractBox" class="spot-contract-box hidden">
                  Contract Program: <strong>Veg Program 25-26</strong><br>
                  Date Range: <strong>10/26/25-10/31/26</strong><br>
                  Available Volume: <strong>100 Weekly</strong><br>
                  Price: <strong>$16.00</strong> (Est on May 16 <strong id="spotContractEstPrice">$16.85</strong>)
                </div>
              </div>
              <div id="spotOnlyWrap" class="hidden">
                <span class="spot-pill-inline">Spot (100%)</span>
                <div class="spot-muted">Contract ignored in Spot Market mode</div>
              </div>
            </td>
            <td>
              <div id="spotIcebergPrice" class="spot-price">$16.85</div>
              <div class="spot-price-sub">Supplier Avg $16.00</div>
            </td>
            <td>
              <div class="spot-good">$2.65 below USDA ↓</div>
              <div class="spot-usda-sub">USDA Avg $48.60 ⓘ</div>
            </td>
          </tr>
          <tr>
            <td>
              <div class="spot-item">Red Onion</div>
              <div class="spot-supplier">Fresh Harvest Co. • Yuma, AZ</div>
            </td>
            <td class="spot-request">100 units</td>
            <td>
              <span class="spot-pill-inline">Spot (100%)</span>
              <div class="spot-muted">No contract on file ⓘ</div>
            </td>
            <td>
              <div class="spot-price">$11.38</div>
              <div class="spot-price-sub">Supplier Avg $12.00</div>
            </td>
            <td>
              <div class="spot-bad">$0.88 above USDA ↑</div>
              <div class="spot-usda-sub">USDA Avg $10.50 ⓘ</div>
            </td>
          </tr>
          <tr>
            <td>
              <div class="spot-item">Broccoli</div>
              <div class="spot-supplier">Valley Fresh Co. • Western, AZ</div>
            </td>
            <td class="spot-request">100 units</td>
            <td>
              <span class="spot-pill-inline">Spot (100%)</span>
              <div class="spot-muted">No contract on file ⓘ</div>
            </td>
            <td>
              <div class="spot-price">$15.43</div>
              <div class="spot-price-sub">Supplier Avg $15.50</div>
            </td>
            <td>
              <div class="spot-good">$8.07 below USDA ↓</div>
              <div class="spot-usda-sub">USDA Avg $23.50 ⓘ</div>
            </td>
          </tr>
        </tbody>
      </table>
      <div class="spot-rec">
        <span>Recommended order:</span>
        <span id="spotRecSuppliers" class="blue">3 Suppliers</span>
        <span>|</span>
        <span id="spotRecPickups" class="blue">3 Pickups</span>
        <span>|</span>
        <span id="spotRecSupplier" class="green">6.6% below supplier Avg.</span>
        <span>|</span>
        <span id="spotRecUsda" class="green">14.4% below USDA</span>
      </div>
    </div>

    <div class="spot-opportunity">
      <div>
        <div id="spotOppTitle" class="spot-opp-title">💡 Optimization Opportunity: Negotiate iceberg lettuce closer to supplier avg in FOB location ($16.00)</div>
        <div id="spotOppSub" class="spot-opp-sub">+ $85 savings with no added pickups</div>
      </div>
      <button class="spot-action" type="button">Negotiate</button>
    </div>

    <div id="spotOrderInsight" class="spot-system"><strong>ⓘ Ai Insight</strong><br>This mix uses the lowest-cost combination across available suppliers while applying contract volume first where it improves savings and keeping pickups unchanged.</div>

    <div class="spot-actions">
      <button class="spot-btn-primary" type="button">Lock Order</button>
      <button class="spot-btn-secondary" type="button">See Alternatives</button>
    </div>

    <div class="spot-foot">Prices include all estimated costs. Estimates update in real time based on market and supplier changes.</div>
  </div>
</div>

<div id="workspaceDrawer" class="workspace-drawer"></div>

<script>
const records = {
  broccoli: {
    id: 'broccoli',
    item: 'Broccoli',
    units: 500,
    fob: 'Oxnard, Ca, CA',
    supplierAvg: 35.45,
    usdaAvg: null,
    shipDate: 'May 16',
    terms: 'FOB daily quote',
    commitmentTotal: 0,
    locked: false,
    flashFields: [],
    flashUntil: 0,
    suppliers: [
      { name: 'Test Farm', quote: 35.45, allocation: 200 },
      { name: 'Newco', quote: 35.45, allocation: 150 },
      { name: 'Conrad Produce', quote: 35.45, allocation: 150 }
    ],
    history: []
  },
  lettuce: {
    id: 'lettuce',
    item: 'Lettuce',
    units: 500,
    fob: 'Oxnard, Ca, CA',
    supplierAvg: 36.35,
    usdaAvg: null,
    shipDate: 'May 16',
    terms: 'FOB daily quote',
    commitmentTotal: 100,
    locked: false,
    flashFields: [],
    flashUntil: 0,
    suppliers: [
      { name: 'Test Farm', quote: 36.35, allocation: 220 },
      { name: 'Newco', quote: 36.35, allocation: 140 },
      { name: 'Conrad Produce', quote: 36.35, allocation: 140 }
    ],
    history: []
  },
  cauliflower: {
    id: 'cauliflower',
    item: 'Cauliflower',
    units: 450,
    fob: 'Oxnard, Ca, CA',
    supplierAvg: 57.17,
    usdaAvg: 42.10,
    shipDate: 'May 18',
    terms: 'FOB market quote',
    commitmentTotal: 0,
    locked: false,
    flashFields: [],
    flashUntil: 0,
    suppliers: [
      { name: 'Test Farm', quote: 57.17, allocation: 150 },
      { name: 'Newco', quote: 57.17, allocation: 150 },
      { name: 'Conrad Produce', quote: 57.17, allocation: 150 }
    ],
    history: []
  },
  spotOptimization: {
    id: 'spotOptimization',
    item: 'Spot Optimization',
    units: 700,
    fob: '3 suppliers · 3 pickups',
    supplierAvg: 0,
    usdaAvg: 0,
    shipDate: 'May 16',
    terms: 'Contract-aware optimization',
    commitmentTotal: 100,
    locked: false,
    flashFields: [],
    flashUntil: 0,
    suppliers: [],
    history: []
  }
};

const workspace = { recordId: null };
let dealBuilt = false;

function money(value){
  return '$' + Number(value).toFixed(2);
}

function pct(value){
  return Math.abs(value).toFixed(1) + '%';
}

function currentRecord(){
  return workspace.recordId ? records[workspace.recordId] : null;
}

function workingPrice(record){
  const totalUnits = record.suppliers.reduce((sum, supplier) => sum + supplier.allocation, 0);
  if (!totalUnits) {
    return record.suppliers.length ? record.suppliers[0].quote : 0;
  }
  const weighted = record.suppliers.reduce((sum, supplier) => sum + supplier.quote * supplier.allocation, 0);
  return weighted / totalUnits;
}

function remainingCommitment(record){
  const applied = Math.min(record.commitmentTotal || 0, record.units);
  return Math.max((record.commitmentTotal || 0) - applied, 0);
}

function usdaDelta(record){
  if (record.usdaAvg == null) {
    return null;
  }
  const diff = Number((workingPrice(record) - record.usdaAvg).toFixed(2));
  const percent = Math.abs(diff / record.usdaAvg * 100);
  return {
    diff,
    percent,
    direction: diff > 0 ? 'over USDA' : diff < 0 ? 'below USDA' : 'at USDA'
  };
}

function supplierDelta(quote, avg){
  const diff = Number((quote - avg).toFixed(2));
  const percent = avg ? Math.abs(diff / avg * 100) : 0;
  return {
    diff,
    percent,
    direction: diff > 0 ? 'over Supplier Avg' : diff < 0 ? 'below Supplier Avg' : 'below Supplier Avg'
  };
}

function fieldClass(record, key){
  return record.flashUntil > Date.now() && record.flashFields.includes(key) ? 'flash' : '';
}

function markChanges(record, fields){
  record.flashFields = fields;
  record.flashUntil = Date.now() + 1500;
  setTimeout(() => {
    if (Date.now() >= record.flashUntil) {
      record.flashFields = [];
      record.flashUntil = 0;
      renderBoard();
    }
  }, 1550);
}

function marketSummaryLines(record){
  const lines = [];
  if (record.usdaAvg != null) {
    lines.push(`<div class="summary-line red">USDA Avg <strong class="${fieldClass(record, 'market')}">${money(record.usdaAvg)}</strong></div>`);
  }
  lines.push(`<div class="summary-line">Supplier Avg <strong class="${fieldClass(record, 'supplierAvg')}">${money(record.supplierAvg)}</strong></div>`);
  return lines.join('');
}

function supplierSlot(record, supplier){
  const sDelta = supplierDelta(supplier.quote, record.supplierAvg);
  const uDelta = record.usdaAvg == null ? null : Number((supplier.quote - record.usdaAvg).toFixed(2));
  const uPct = record.usdaAvg ? Math.abs(uDelta / record.usdaAvg * 100) : 0;
  const uClass = uDelta > 0 ? 'red' : 'green';
  const sClass = sDelta.diff > 0 ? 'red' : 'green';
  const usdaLine = record.usdaAvg == null ? '' : `<div class="slot-delta ${uClass}"><span class="${fieldClass(record, 'deltas')}">${money(Math.abs(uDelta))} ${uDelta > 0 ? 'over USDA' : uDelta < 0 ? 'below USDA' : 'at USDA'} (${pct(uPct)})</span></div>`;
  const supplierLine = `<div class="slot-delta ${sClass}"><span class="${fieldClass(record, 'deltas')}">${money(Math.abs(sDelta.diff))} ${sDelta.diff > 0 ? 'over Supplier Avg' : 'below Supplier Avg'} (${pct(sDelta.percent)})</span></div>`;

  return `
    <div class="supplier-slot">
      <div>
        <div class="slot-label">Target Price</div>
        <div class="slot-price"><span class="${fieldClass(record, 'price')}">${money(supplier.quote)}</span> / unit (case)</div>
        <div class="slot-quote">Quote <strong class="${fieldClass(record, 'quote')}">${money(supplier.quote)}</strong> / unit (case)</div>
        ${usdaLine}
        ${supplierLine}
      </div>
      <div class="supplier-name">${supplier.name}</div>
    </div>
  `;
}

function cardMarkup(record){
  const isActive = workspace.recordId === record.id;
  const activeClass = isActive ? ' active' : '';
  const inactiveClass = workspace.recordId && !isActive ? ' inactive' : '';
  const changedClass = record.flashUntil > Date.now() ? ' changed' : '';
  const status = record.locked ? '<span class="locked-pill">Locked</span>' : (isActive ? '<span class="active-pill">Workspace Open</span>' : '');

  return `
    <div id="card-${record.id}" class="commodity-card${activeClass}${inactiveClass}${changedClass}" data-record="${record.id}">
      <div class="card-head">
        <div class="card-head-row">
          <div class="card-label">Supplier Prices</div>
          <div>${status}</div>
        </div>
        <div class="card-header-row">
          <div>
            <div class="card-title">${record.item} <span class="card-units ${fieldClass(record, 'units')}">${record.units} units</span></div>
            <div class="card-meta">FOB: ${record.fob}</div>
          </div>
          <div class="card-summary">${marketSummaryLines(record)}</div>
        </div>
      </div>
      ${record.suppliers.map(supplier => supplierSlot(record, supplier)).join('')}
    </div>
  `;
}

function inlineWorkspaceMarkup(record){
  return `
    <div class="workspace-chat">
      <div class="workspace-top">
        <div class="workspace-title">${record.item} Workspace Chat</div>
        <button id="wsClose" class="close-btn" type="button">Close</button>
      </div>
      <div class="quick-prompts">
        <button class="quick-prompt" type="button" data-prompt="Improve Pricing">Improve Pricing</button>
        <button class="quick-prompt" type="button" data-prompt="Match Lowest Supplier">Match Lowest Supplier</button>
        <button class="quick-prompt" type="button" data-prompt="Add more suppliers">Add more suppliers</button>
        <button class="quick-prompt" type="button" data-prompt="Lock Deal">Lock Deal</button>
      </div>
      <div id="wsThread" class="thread"></div>
      <div class="composer-wrap">
        <div class="composer-shell">
          <textarea id="wsComposer" class="composer" placeholder="Use this workspace to improve pricing, optimize supplier mix, and prepare the final deal."></textarea>
          <button id="wsSend" class="send-btn" type="button" aria-label="Send">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M22 2L11 13"></path>
              <path d="M22 2L15 22L11 13L2 9L22 2Z"></path>
            </svg>
          </button>
        </div>
        <div class="composer-note">Enter sends. Shift+Enter adds a new line.</div>
      </div>
    </div>
  `;
}

function renderBoard(){
  const grid = document.getElementById('boardGrid');
  const shell = document.getElementById('mainShell');
  const drawer = document.getElementById('workspaceDrawer');
  const spotShell = document.getElementById('spotShell');
  const buildDealBtn = document.getElementById('buildDealBtn');
  const activeRecord = currentRecord();
  const boardRecords = Object.values(records).filter(record => record.id !== 'spotOptimization');
  const ordered = activeRecord
    ? (activeRecord.id === 'spotOptimization'
      ? boardRecords
      : [activeRecord, ...boardRecords.filter(record => record.id !== activeRecord.id)])
    : boardRecords;

  let markup = '';
  ordered.forEach((record) => {
    markup += cardMarkup(record);
  });

  grid.classList.toggle('workspace-open', Boolean(activeRecord));
  shell.classList.toggle('drawer-open', Boolean(activeRecord));
  if (spotShell) {
    spotShell.classList.toggle('hidden', !dealBuilt);
    spotShell.classList.toggle('active', workspace.recordId === 'spotOptimization');
  }
  if (buildDealBtn) {
    buildDealBtn.style.display = dealBuilt ? 'none' : 'inline-flex';
  }
  grid.innerHTML = markup;
  bindBoardClicks();

  if (activeRecord) {
    drawer.innerHTML = inlineWorkspaceMarkup(activeRecord);
    drawer.classList.add('open');
    bindWorkspace();
    renderWorkspaceThread();
    updateDrawerPosition();
  } else {
    drawer.innerHTML = '';
    drawer.classList.remove('open');
    drawer.style.top = '';
    drawer.style.maxHeight = '';
  }
}

function bindBoardClicks(){
  document.querySelectorAll('.commodity-card').forEach(card => {
    if (card.dataset.bound === 'true') {
      return;
    }
    card.dataset.bound = 'true';
    card.addEventListener('click', () => openWorkspace(card.dataset.record));
  });
  const spotShell = document.getElementById('spotShell');
  if (spotShell && !spotShell.dataset.boundWorkspace) {
    spotShell.dataset.boundWorkspace = 'true';
    spotShell.addEventListener('click', () => openWorkspace('spotOptimization'));
  }
  const buildDealBtn = document.getElementById('buildDealBtn');
  if (buildDealBtn && !buildDealBtn.dataset.boundBuildDeal) {
    buildDealBtn.dataset.boundBuildDeal = 'true';
    buildDealBtn.addEventListener('click', event => {
      event.stopPropagation();
      dealBuilt = true;
      renderBoard();
      const visibleSpotShell = document.getElementById('spotShell');
      if (visibleSpotShell) {
        visibleSpotShell.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  }
}

function bindWorkspace(){
  const send = document.getElementById('wsSend');
  const close = document.getElementById('wsClose');
  const composer = document.getElementById('wsComposer');
  if (send) send.addEventListener('click', handleMessage);
  if (close) close.addEventListener('click', closeWorkspace);
  document.querySelectorAll('.quick-prompt').forEach(button => {
    button.addEventListener('click', () => runQuickPrompt(button.dataset.prompt));
  });
  if (composer) {
    composer.addEventListener('keydown', event => {
      if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        handleMessage();
      }
    });
  }
}

function openWorkspace(recordId){
  workspace.recordId = recordId;
  renderBoard();
  const activeCard = document.getElementById(`card-${recordId}`);
  if (activeCard) {
    activeCard.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
  setTimeout(updateDrawerPosition, 60);
}

function closeWorkspace(){
  workspace.recordId = null;
  renderBoard();
}

function normalizeSupplierName(text, record){
  return record.suppliers.find(supplier => text.toLowerCase().includes(supplier.name.toLowerCase()));
}

function parseAllocations(text, record){
  const updates = [];
  record.suppliers.forEach(supplier => {
    const escaped = supplier.name.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const before = new RegExp('(\\d+)\\s*(?:units?|cases?)\\s*(?:to|for)?\\s*' + escaped, 'i');
    const after = new RegExp(escaped + '\\s*(?:to|for)?\\s*(\\d+)\\s*(?:units?|cases?)', 'i');
    const match = text.match(before) || text.match(after);
    if (match) {
      updates.push({ name: supplier.name, allocation: Number(match[1]) });
    }
  });
  return updates;
}

function parseProposal(text, record){
  const proposal = {};
  const priceMatch = text.match(/\$?\s*(\d+(?:\.\d+)?)/);
  if (/(price|quote|target)/i.test(text) && priceMatch) {
    proposal.price = Number(priceMatch[1]);
  } else if (/supplier avg|match avg|move to avg/i.test(text)) {
    proposal.price = record.supplierAvg;
  } else if (/reduce|lower|cheaper|improve/i.test(text) && record.usdaAvg != null && workingPrice(record) > record.usdaAvg) {
    proposal.price = Number((workingPrice(record) - 1).toFixed(2));
  }

  const unitsMatch = text.match(/(?:total|quantity|units?)\s*(?:to|at)?\s*(\d+)/i);
  if (unitsMatch) {
    proposal.units = Number(unitsMatch[1]);
  }

  const shipMatch = text.match(/(?:ship date|date)\s*(?:to|for)?\s*([A-Za-z]{3,9}\s+\d{1,2})/i);
  if (shipMatch) {
    proposal.shipDate = shipMatch[1];
  }

  const termsMatch = text.match(/terms?\s*(?:to|as|=)?\s*([^\n.]+)/i);
  if (termsMatch) {
    proposal.terms = termsMatch[1].trim();
  }

  const allocations = parseAllocations(text, record);
  if (allocations.length) {
    proposal.allocations = allocations;
  }

  const supplierPick = normalizeSupplierName(text, record);
  if (/switch|move|use|allocate all|all to/i.test(text) && supplierPick) {
    proposal.singleSupplier = supplierPick.name;
  }

  if (/lock/i.test(text)) {
    proposal.locked = true;
  }

  return proposal;
}

function applyProposal(record, proposal){
  const changes = [];
  const flashFields = new Set();

  if (proposal.price != null && proposal.price > 0) {
    const currentWorking = workingPrice(record);
    const totalAllocated = record.suppliers.reduce((sum, supplier) => sum + supplier.allocation, 0) || record.units;
    record.suppliers.forEach(supplier => {
      const ratio = totalAllocated ? supplier.allocation / totalAllocated : 1 / record.suppliers.length;
      const weightedMove = supplier.quote + (proposal.price - currentWorking) * Math.max(ratio, 0.2);
      supplier.quote = Number(weightedMove.toFixed(2));
    });
    const lead = record.suppliers.reduce((best, supplier) => supplier.allocation > best.allocation ? supplier : best, record.suppliers[0]);
    if (lead) {
      lead.quote = Number(proposal.price.toFixed(2));
    }
    changes.push('price');
    ['price','quote','deltas'].forEach(field => flashFields.add(field));
  }

  if (proposal.units != null && proposal.units > 0) {
    record.units = proposal.units;
    const total = record.suppliers.reduce((sum, supplier) => sum + supplier.allocation, 0);
    if (total > 0) {
      let running = 0;
      record.suppliers.forEach((supplier, index) => {
        if (index === record.suppliers.length - 1) {
          supplier.allocation = record.units - running;
        } else {
          supplier.allocation = Math.round(record.units * (supplier.allocation / total));
          running += supplier.allocation;
        }
      });
    }
    changes.push('units');
    flashFields.add('units');
  }

  if (proposal.shipDate) {
    record.shipDate = proposal.shipDate;
    changes.push('ship date');
  }

  if (proposal.terms) {
    record.terms = proposal.terms;
    changes.push('terms');
  }

  if (proposal.singleSupplier) {
    record.suppliers.forEach(supplier => {
      supplier.allocation = supplier.name === proposal.singleSupplier ? record.units : 0;
    });
    changes.push('supplier mix');
    flashFields.add('quote');
  } else if (proposal.allocations && proposal.allocations.length) {
    let allocated = 0;
    proposal.allocations.forEach(update => {
      const supplier = record.suppliers.find(entry => entry.name === update.name);
      if (supplier) {
        supplier.allocation = update.allocation;
        allocated += update.allocation;
      }
    });
    const untouched = record.suppliers.filter(entry => !proposal.allocations.find(update => update.name === entry.name));
    if (untouched.length) {
      const remainder = Math.max(record.units - allocated, 0);
      const even = Math.floor(remainder / untouched.length);
      let running = 0;
      untouched.forEach((supplier, index) => {
        supplier.allocation = index === untouched.length - 1 ? remainder - running : even;
        running += supplier.allocation;
      });
    }
    changes.push('allocation');
    flashFields.add('quote');
  }

  if (proposal.locked) {
    record.locked = true;
    changes.push('lock status');
  }

  if (changes.length) {
    markChanges(record, Array.from(flashFields.size ? flashFields : new Set(['quote'])));
  }

  return changes;
}

function commodityReasoning(record){
  const price = workingPrice(record);
  const topSupplier = record.suppliers.reduce((best, supplier) => supplier.allocation > best.allocation ? supplier : best, record.suppliers[0]);
  const mixSummary = record.suppliers
    .filter(supplier => supplier.allocation > 0)
    .map(supplier => `${supplier.allocation} units with ${supplier.name}`)
    .join(', ');

  if (record.usdaAvg != null) {
    const delta = usdaDelta(record);
    if (delta.diff > 0) {
      return `This mix is still ${money(Math.abs(delta.diff))} over USDA, driven mostly by ${topSupplier.name} at ${money(topSupplier.quote)}. To improve it, lower the lead quote or shift more volume to a supplier willing to clear below ${money(record.usdaAvg)}. Current live mix: ${mixSummary}.`;
    }
    return `This mix is below USDA and concentrated around ${topSupplier.name}, with a current working price of ${money(price)}. The live card favors the lowest effective market position without adding extra supplier complexity. Current live mix: ${mixSummary}.`;
  }

  return `This mix is centered around ${topSupplier.name} at a working price of ${money(price)}. Because USDA is not the primary anchor here, the recommendation is optimizing against supplier average and allocation balance. Current live mix: ${mixSummary}.`;
}

function compareReply(record){
  const ranked = [...record.suppliers].sort((a, b) => a.quote - b.quote);
  const best = ranked[0];
  const second = ranked[1];
  if (!second) {
    return `Only one supplier is currently active on this card. ${best.name} is the live recommendation at ${money(best.quote)}.`;
  }
  return `${best.name} is currently the best price at ${money(best.quote)}. ${second.name} trails by ${money(Math.abs(second.quote - best.quote))}. I can reallocate more units to ${best.name}, test a lower target, or explain the tradeoff against the current mix.`;
}

function runQuickPrompt(prompt){
  const composer = document.getElementById('wsComposer');
  if (!composer) {
    return;
  }
  composer.value = prompt;
  handleMessage();
}

const spotState = {
  mode: 'contract',
  demand: 500,
  contractedVolume: 100,
  otherSpot: 200,
  contractPrice: 16.10,
  spotPrice: 16.85,
  onionTotal: 100 * 11.38,
  broccoliTotal: 100 * 15.43,
  recommendedSavings: 169,
  recommendedSupplierSavings: 123,
  supplierCount: 3,
  pickups: 3
};

spotState.recommendedTotal =
  spotState.contractedVolume * spotState.contractPrice +
  (spotState.demand - spotState.contractedVolume) * spotState.spotPrice +
  spotState.onionTotal +
  spotState.broccoliTotal;

function updateSpotOptimization(){
  const slider = document.getElementById('spotSplitSlider');
  if (!slider) {
    return;
  }

  const isMarket = spotState.mode === 'market';
  const requestedContract = isMarket ? 0 : Number(slider.value);
  const guaranteedContract = isMarket ? 0 : Math.min(requestedContract, spotState.contractedVolume);
  const icebergSpot = spotState.demand - requestedContract;
  const economicSpotUnits = spotState.demand - guaranteedContract;
  const totalSpot = economicSpotUnits + spotState.otherSpot;
  const total =
    guaranteedContract * spotState.contractPrice +
    economicSpotUnits * spotState.spotPrice +
    spotState.onionTotal +
    spotState.broccoliTotal;
  const loss = Math.round(total - spotState.recommendedTotal);
  const savings = spotState.recommendedSavings - loss;
  const supplierSavings = spotState.recommendedSupplierSavings - loss;
  const contractPct = Math.round((requestedContract / spotState.demand) * 100);
  const spotPct = 100 - contractPct;
  const usdaPct = (savings / spotState.recommendedSavings * 12.8).toFixed(1);
  const supplierPct = (supplierSavings / spotState.recommendedSupplierSavings * 7.4).toFixed(1);
  const recSupplierPct = (supplierSavings / spotState.recommendedSupplierSavings * 6.6).toFixed(1);
  const recUsdaPct = (savings / spotState.recommendedSavings * 14.4).toFixed(1);

  document.getElementById('spotBarContract').style.width = `${contractPct}%`;
  document.getElementById('spotBarSpot').style.width = `${spotPct}%`;
  document.getElementById('spotBarContract').textContent = `${contractPct}%`;
  document.getElementById('spotBarSpot').textContent = `${spotPct}%`;
  document.getElementById('spotBarHandle').style.left = `${contractPct}%`;

  document.getElementById('spotContractText').textContent = `${requestedContract} contract`;
  document.getElementById('spotSpotText').textContent = `${icebergSpot} spot`;
  document.getElementById('spotTopContract').textContent = `${requestedContract} units`;
  document.getElementById('spotTopSpot').textContent = `${totalSpot} units`;
  document.getElementById('spotInsightContract').textContent = `${requestedContract} units`;
  document.getElementById('spotInsightSpot').textContent = `${totalSpot} units`;
  document.getElementById('spotInsightHead').textContent = `$${Math.round(savings)} below USDA across all items`;
  document.getElementById('spotMetricUsda').textContent = `$${Math.round(savings)} below`;
  document.getElementById('spotMetricUsdaPct').textContent = `(-${usdaPct}%)`;
  document.getElementById('spotMetricSupplier').textContent = `$${Math.round(supplierSavings)} below`;
  document.getElementById('spotMetricSupplierPct').textContent = `(-${supplierPct}%)`;
  document.getElementById('spotIcebergPrice').textContent = `$${spotState.spotPrice.toFixed(2)}`;
  document.getElementById('spotContractEstPrice').textContent = `$${spotState.spotPrice.toFixed(2)}`;
  document.getElementById('spotRecSuppliers').textContent = `${spotState.supplierCount} Suppliers`;
  document.getElementById('spotRecPickups').textContent = `${spotState.pickups} Pickups`;
  document.getElementById('spotRecSupplier').textContent = `${recSupplierPct}% below supplier Avg.`;
  document.getElementById('spotRecUsda').textContent = `${recUsdaPct}% below USDA`;
  document.getElementById('spotOverNote').style.display = requestedContract > spotState.contractedVolume ? 'block' : 'none';
  document.getElementById('spotContractWrap').classList.toggle('hidden', isMarket);
  document.getElementById('spotOnlyWrap').classList.toggle('hidden', !isMarket);
  document.getElementById('spotModeContract').classList.toggle('active', !isMarket);
  document.getElementById('spotModeMarket').classList.toggle('active', isMarket);
  document.getElementById('spotModePill').textContent = isMarket ? 'Spot Market' : 'Contract-Aware';
  document.getElementById('spotModeSub').textContent = isMarket
    ? 'AI optimized demand without applying contract commitments.'
    : 'AI optimized demand while respecting contract commitments.';
  document.getElementById('spotOppTitle').textContent = spotState.spotPrice <= 16
    ? '💡 Optimization Opportunity: Supplier-average pricing applied to iceberg lettuce in FOB location ($16.00)'
    : '💡 Optimization Opportunity: Negotiate iceberg lettuce closer to supplier avg in FOB location ($16.00)';
  document.getElementById('spotOppSub').textContent = spotState.spotPrice <= 16
    ? '+ $85 savings captured with no added pickups'
    : '+ $85 savings with no added pickups';

  const mixText = isMarket
    ? 'This mix is recommended because it uses the lowest-cost spot combination across available suppliers without applying any contract coverage.'
    : requestedContract > spotState.contractedVolume
    ? 'This mix is still recommended because it holds the lowest-cost supplier combination, applies all available contract coverage first, and only pushes excess iceberg demand into spot where needed.'
    : 'This mix uses the lowest-cost combination across available suppliers while applying contract volume first where it improves savings and keeping pickups unchanged.';
  document.getElementById('spotOrderInsight').innerHTML = `<strong>ⓘ Ai Insight</strong><br>${mixText}`;
}

function setSpotMode(nextMode){
  spotState.mode = nextMode;
  updateSpotOptimization();
}

function handleSpotWorkspaceMessage(text){
  const lower = text.toLowerCase();
  const changes = [];
  if (/spot market|spot only/.test(lower)) {
    setSpotMode('market');
    changes.push('mode');
  }
  if (/contract aware|use contract/.test(lower)) {
    setSpotMode('contract');
    changes.push('mode');
  }

  const priceMatch = text.match(/\$?\s*(\d+(?:\.\d+)?)/);
  if (/(price|quote|improve pricing|match lowest supplier|lower)/i.test(text)) {
    if (priceMatch) {
      spotState.spotPrice = Number(priceMatch[1]);
    } else if (/match lowest supplier|improve pricing/i.test(text)) {
      spotState.spotPrice = 16.00;
    }
    changes.push('price');
  }

  const contractMatch = text.match(/contract(?:\s+to)?\s+(\d+)/i);
  if (contractMatch && spotState.mode === 'contract') {
    const slider = document.getElementById('spotSplitSlider');
    if (slider) {
      slider.value = contractMatch[1];
    }
    changes.push('contract split');
  }

  if (/add more suppliers/i.test(lower)) {
    spotState.supplierCount = 4;
    spotState.pickups = 4;
    changes.push('supplier coverage');
  }

  if (/lock/i.test(lower)) {
    records.spotOptimization.locked = true;
    changes.push('lock status');
  }

  updateSpotOptimization();
  return changes;
}

function updateDrawerPosition(){
  const record = currentRecord();
  const drawer = document.getElementById('workspaceDrawer');
  const card = !record ? null : record.id === 'spotOptimization'
    ? document.getElementById('spotShell')
    : document.getElementById(`card-${record.id}`);
  if (!drawer || !card || !drawer.classList.contains('open')) {
    return;
  }

  const cardRect = card.getBoundingClientRect();
  const viewportHeight = window.innerHeight;
  const gap = 4;
  const minHeight = 260;
  const maxHeight = 360;
  const available = Math.max(viewportHeight - cardRect.bottom - gap - 16, minHeight);
  const drawerHeight = Math.min(maxHeight, available);
  const top = Math.min(cardRect.bottom + gap, viewportHeight - drawerHeight - 8);

  drawer.style.top = `${Math.max(8, top)}px`;
  drawer.style.maxHeight = `${drawerHeight}px`;
}

function renderWorkspaceThread(){
  const record = currentRecord();
  const thread = document.getElementById('wsThread');
  if (!record || !thread) {
    return;
  }
  thread.innerHTML = record.history.map(message => `<div class="msg ${message.role}">${message.text}</div>`).join('');
  thread.scrollTop = thread.scrollHeight;
}

function handleMessage(){
  const record = currentRecord();
  const composer = document.getElementById('wsComposer');
  const text = composer ? composer.value.trim() : '';
  if (!record || !text) {
    return;
  }

  record.history.push({ role: 'user', text });
  if (record.id === 'spotOptimization') {
    const changes = handleSpotWorkspaceMessage(text);
    const reply = changes.length
      ? `Updated the Spot Optimization object immediately. I changed ${changes.join(', ')} and refreshed the live optimization card.`
      : 'I reviewed the Spot Optimization object. Ask me to improve pricing, switch between Contract Aware and Spot Market, change contract units, add suppliers, or lock the final mix.';
    record.history.push({ role: 'ai', text: reply });
    if (composer) {
      composer.value = '';
    }
    renderBoard();
    return;
  }
  const proposal = parseProposal(text, record);
  let reply = '';

  if (/match lowest supplier/i.test(text)) {
    const lowest = Math.min(...record.suppliers.map(supplier => supplier.quote));
    const changes = applyProposal(record, { price: lowest });
    reply = `Matched the live working price to the lowest supplier signal at ${money(lowest)} and refreshed the selected quote card. ${commodityReasoning(record)}`;
  } else if (/add more suppliers/i.test(text)) {
    const supplierName = `Alt Supplier ${record.suppliers.length - 2}`;
    const quote = Number((workingPrice(record) - 0.35).toFixed(2));
    record.suppliers.push({
      name: supplierName,
      quote,
      allocation: 0
    });
    markChanges(record, ['quote']);
    reply = `Added ${supplierName} to the live quote card at ${money(quote)} so you can compare a broader supplier set without changing the current allocation yet.`;
  } else if (/improve pricing/i.test(text)) {
    const target = record.usdaAvg != null
      ? Number((workingPrice(record) - 1).toFixed(2))
      : Number((Math.min(workingPrice(record), record.supplierAvg) - 0.25).toFixed(2));
    const changes = applyProposal(record, { price: Math.max(target, 0.01) });
    reply = `Improved pricing on the selected quote card and refreshed the live deltas. ${commodityReasoning(record)}`;
  } else if (Object.keys(proposal).length) {
    const changes = applyProposal(record, proposal);
    if (changes.length) {
      reply = `Updated the selected quote card immediately. I changed ${changes.join(', ')} and refreshed the live deltas on the card. ${commodityReasoning(record)}`;
    } else {
      reply = 'I understood the request, but it did not create a net change in the selected quote card.';
    }
  } else if (/compare|best|better|worse|why/i.test(text)) {
    reply = compareReply(record);
  } else if (/lock/i.test(text)) {
    record.locked = true;
    markChanges(record, ['quote']);
    reply = 'Locked the selected quote card. The update stays reflected on the card when you return to Main Chat.';
  } else {
    reply = `I reviewed the selected live quote card for ${record.item}. Ask for a concrete price, supplier, allocation, unit, ship date, term, or lock change and I will update that card directly.`;
  }

  record.history.push({ role: 'ai', text: reply });
  if (composer) {
    composer.value = '';
  }
  renderBoard();
}

window.addEventListener('resize', updateDrawerPosition);
window.addEventListener('scroll', updateDrawerPosition, { passive: true });

document.getElementById('spotSplitSlider').addEventListener('input', updateSpotOptimization);
document.getElementById('spotModeContract').addEventListener('click', () => setSpotMode('contract'));
document.getElementById('spotModeMarket').addEventListener('click', () => setSpotMode('market'));
document.getElementById('spotContractToggle').addEventListener('click', event => {
  event.stopPropagation();
  document.getElementById('spotContractBox').classList.toggle('hidden');
});
['spotSplitSlider','spotModeContract','spotModeMarket'].forEach(id => {
  const el = document.getElementById(id);
  if (el) {
    el.addEventListener('click', event => event.stopPropagation());
    el.addEventListener('mousedown', event => event.stopPropagation());
  }
});
updateSpotOptimization();
renderBoard();
</script>
</body>
</html>
"""


html(APP_HTML, height=1220, scrolling=True)
