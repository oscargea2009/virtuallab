from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = r"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Virtual Electronics Research Lab</title>
  <style>
    body { margin: 0; padding: 16px; background: #08111b; }
    #veLab{font-family:Inter,Arial,sans-serif;color:#e8f0f7;background:#0d1825;border:1px solid #29445b;border-radius:18px;padding:14px;max-width:1200px;margin:0 auto;box-sizing:border-box}
    #veLab *{box-sizing:border-box}
    #veLab .hero{padding:18px 20px;border-radius:13px;background:linear-gradient(125deg,#102b42,#17536a 70%,#087d79);margin-bottom:12px}
    #veLab .hero h2{font-size:22px;letter-spacing:.4px;margin:0 0 5px;color:#56ead6}
    #veLab .hero p{font-size:12px;line-height:1.5;margin:0;color:#d2e6ef}
    #veLab .layout{display:grid;grid-template-columns:minmax(0,1.7fr) minmax(270px,1fr);gap:12px;align-items:start}
    #veLab .card{background:#142437;border:1px solid #29455e;border-radius:13px;padding:13px;margin-bottom:12px;min-width:0}
    #veLab .card h3{font-size:14px;color:#55ddcb;margin:0 0 10px}
    #veLab .canvasWrap{background:#101d2b;border:1px solid #36536a;border-radius:12px;overflow:hidden}
    #veLab canvas{display:block;width:100%;height:auto;touch-action:none}
    #veLab #bench{cursor:crosshair}
    #veLab .legend{display:flex;gap:12px;flex-wrap:wrap;padding:9px 3px 2px;color:#a9bdce;font-size:10px}
    #veLab .swatch{display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:5px}
    #veLab .field{margin:10px 0}
    #veLab label{display:flex;justify-content:space-between;gap:8px;color:#bbccda;font-size:11px;margin-bottom:6px}
    #veLab output{font-weight:700;color:#69e6d4}
    #veLab input[type=range]{width:100%;accent-color:#32cdbd;cursor:pointer}
    #veLab select{width:100%;padding:9px;background:#0e1c2a;color:#e8f0f7;border:1px solid #3a586e;border-radius:8px}
    #veLab .btnrow{display:flex;flex-wrap:wrap;gap:7px;margin:8px 0}
    #veLab button{background:#213950;color:#eaf3f8;border:1px solid #3b5b72;border-radius:8px;padding:9px 11px;font-size:11px;font-weight:700;cursor:pointer;transition:.14s}
    #veLab button:hover{background:#2d526d;transform:translateY(-1px)}
    #veLab button.active{background:#087c75;border-color:#42d8c7;color:#fff}
    #veLab button.warn{background:#593d22;border-color:#a67539}
    #veLab button.red{background:#572d37;border-color:#a54b5a}
    #veLab button:disabled{opacity:.4;cursor:not-allowed;transform:none}
    #veLab .presets button{padding:6px 8px;font-size:10px}
    #veLab .hint{font-size:10px;line-height:1.6;color:#91a9ba;margin-top:8px}
    #veLab .status{background:#0c1926;border:1px solid #294358;border-left:4px solid #39cdbd;border-radius:8px;padding:10px;font-size:11px;line-height:1.55;color:#d7e5ee;margin-top:10px}
    #veLab .status.bad{border-left-color:#f06a6a}
    #veLab .status.warn{border-left-color:#e7ad55}
    #veLab .metrics{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;margin-top:12px}
    #veLab .metric{background:#0d1c2a;border:1px solid #28465c;border-radius:9px;padding:10px;min-width:0}
    #veLab .metric small{display:block;color:#90aabc;font-size:9px;margin-bottom:5px}
    #veLab .metric b{display:block;color:#58e1ce;font-size:16px;overflow-wrap:anywhere}
    #veLab .submetric{font-size:10px;color:#b6c8d5;line-height:1.7;margin-top:8px;white-space:pre-line}
    #veLab .tableWrap{overflow-x:auto;border:1px solid #2b465b;border-radius:9px}
    #veLab table{border-collapse:collapse;width:100%;min-width:720px;font-size:10px}
    #veLab th{background:#1b344a;color:#7ee7d8;text-align:left;padding:8px;white-space:nowrap}
    #veLab td{border-top:1px solid #273f54;padding:7px;color:#d4e0e9;white-space:nowrap}
    #veLab tr:nth-child(even) td{background:#102033}
    #veLab #chart{background:#0c1926;border:1px solid #29465d;border-radius:10px;width:100%;height:auto}
    #veLab .two{display:grid;grid-template-columns:1fr 1fr;gap:8px}
    #veLab .sectionLabel{font-size:10px;color:#8fa9ba;margin:13px 0 5px;font-weight:700;letter-spacing:.5px}
    #veLab .footer{font-size:9px;text-align:center;color:#758d9f;padding:5px}
    @media(max-width:850px){#veLab .layout{grid-template-columns:1fr}#veLab .metrics{grid-template-columns:repeat(2,minmax(0,1fr))}}
    @media(max-width:460px){#veLab{padding:8px}#veLab .hero h2{font-size:17px}#veLab .metrics{grid-template-columns:1fr 1fr}#veLab button{font-size:10px;padding:8px}}
  </style>
</head>
<body>
<div id="veLab">
  <div class="hero">
    <h2>⚡ VIRTUAL ELECTRONICS RESEARCH LAB</h2>
    <p>PENGARUH HAMBATAN TERHADAP ARUS LISTRIK — RANGKAIAN SERI &amp; PARALEL</p>
    <p>Bangun rangkaian, geser resistor, hubungkan probe, ukur, catat data, dan ekspor hasil penelitian.</p>
  </div>

  <div class="layout">
    <section>
      <div class="card">
        <h3>MEJA KERJA &amp; EDITOR RANGKAIAN</h3>
        <div class="canvasWrap"><canvas id="bench" width="1200" height="760"></canvas></div>
        <div class="legend">
          <span><i class="swatch" style="background:#ff5656"></i>Probe merah (+)</span>
          <span><i class="swatch" style="background:#111827;border:1px solid #9fb4c4"></i>Probe hitam (COM)</span>
          <span><i class="swatch" style="background:#f0cb72"></i>Resistor / filamen</span>
          <span><i class="swatch" style="background:#4ce0c9"></i>Jalur aktif</span>
        </div>
        <div class="hint">Interaksi kanvas: klik resistor untuk memilihnya; tarik resistor untuk mengatur posisi visual; tarik ujung probe ke terminal yang menyala. Sambungan kabel rangkaian otomatis mengikuti topologi seri/paralel.</div>
      </div>

      <div class="card">
        <h3>HASIL PENGUKURAN &amp; BESARAN LISTRIK</h3>
        <div class="metrics">
          <div class="metric"><small>HAMBATAN EKUIVALEN</small><b id="mReq">—</b></div>
          <div class="metric"><small>ARUS TOTAL MODEL</small><b id="mI">—</b></div>
          <div class="metric"><small>ARUS IDEAL V / Req</small><b id="mIdeal">—</b></div>
          <div class="metric"><small>TEGANGAN PADA BEBAN</small><b id="mVload">—</b></div>
          <div class="metric"><small>PEMBACAAN MULTIMETER</small><b id="mMeter">—</b></div>
          <div class="metric"><small>STATUS SEKRING</small><b id="mFuse">—</b></div>
        </div>
        <div class="submetric" id="branchInfo">Arus cabang akan ditampilkan di sini.</div>
        <div class="status" id="measurementStatus">Siap. Hubungkan probe sesuai mode multimeter.</div>
      </div>

      <div class="card">
        <h3>GRAFIK PENELITIAN: ARUS TOTAL vs HAMBATAN EKUIVALEN</h3>
        <canvas id="chart" width="900" height="330"></canvas>
        <div class="hint">Sumbu-X menggunakan skala logaritmik karena rentang resistor dapat berbeda jauh. Titik data berasal dari percobaan yang dicatat. Warna biru kehijauan = seri; warna jingga = paralel.</div>
      </div>
    </section>

    <aside>
      <div class="card">
        <h3>1. RANCANGAN RANGKAIAN</h3>
        <div class="sectionLabel">TOPOLOGI</div>
        <div class="btnrow">
          <button id="topSeries" class="active">Rangkaian Seri</button>
          <button id="topParallel">Rangkaian Paralel</button>
        </div>
        <div class="sectionLabel">KOMPONEN RESISTOR</div>
        <div class="btnrow">
          <button id="addR">＋ Tambah resistor</button>
          <button id="removeR" class="red">− Hapus terpilih</button>
          <button id="resetLayout">↺ Tata ulang</button>
        </div>
        <div class="field">
          <label><span>Resistor terpilih</span><output id="selectedName">R1</output></label>
          <label><span>Nilai hambatan (log slider)</span><output id="rValue">100 Ω</output></label>
          <input id="rSlider" type="range" min="0" max="400" step="1" value="200">
        </div>
        <div class="btnrow presets">
          <button data-r="10">10 Ω</button><button data-r="22">22 Ω</button>
          <button data-r="47">47 Ω</button><button data-r="100">100 Ω</button>
          <button data-r="220">220 Ω</button><button data-r="470">470 Ω</button>
          <button data-r="1000">1 kΩ</button><button data-r="2200">2,2 kΩ</button>
          <button data-r="4700">4,7 kΩ</button>
        </div>
        <div class="hint">Rentang nilai tiap resistor: 1 Ω sampai 10.000 Ω. Slider berskala logaritmik agar nilai kecil dan besar dapat diatur dengan presisi yang lebih baik.</div>
      </div>

      <div class="card">
        <h3>2. SUMBER &amp; PROTEKSI SEKRING</h3>
        <div class="field">
          <label><span>Tegangan sumber DC</span><output id="voltageValue">12.0 V</output></label>
          <input id="voltageSlider" type="range" min="1" max="24" step="0.5" value="12">
        </div>
        <div class="two">
          <div><label><span>Rating sekring</span></label>
            <select id="fuseRating"><option value="0.1">0,10 A</option><option value="0.25">0,25 A</option><option value="0.5">0,50 A</option><option value="1" selected>1,00 A</option><option value="2">2,00 A</option><option value="5">5,00 A</option></select>
          </div>
          <div><label><span>Sumber</span></label><button id="sourceToggle" class="active" style="width:100%">Sumber ON</button></div>
        </div>
        <div class="btnrow"><button id="resetFuse" class="warn">Reset sekring</button></div>
        <div class="hint">Model sekring memakai akumulasi beban lebih sederhana (pendekatan termal I²t). Ini untuk demonstrasi proteksi, bukan kurva putus resmi produsen sekring.</div>
      </div>

      <div class="card">
        <h3>3. MULTIMETER DIGITAL &amp; ANALOG</h3>
        <div class="sectionLabel">MODE PENGUKURAN</div>
        <div class="btnrow">
          <button id="modeA" class="active">A — Arus</button>
          <button id="modeV">V — Tegangan</button>
          <button id="modeOhm">Ω — Hambatan</button>
        </div>
        <div class="btnrow">
          <button id="autoConnect">⛓ Pasang probe sesuai mode</button>
          <button id="disconnect">Lepas kedua probe</button>
        </div>
        <div class="field"><label><span>Rentang amperemeter analog</span></label><select id="analogRange"><option value="0.1">0–0,1 A</option><option value="0.5">0–0,5 A</option><option value="1" selected>0–1 A</option><option value="5">0–5 A</option></select></div>
        <div class="hint"><b>A:</b> probe dimasukkan pada celah ukur arus (seri). <b>V:</b> probe dipasang pada dua terminal beban (paralel). <b>Ω:</b> sumber wajib OFF dan probe pada dua terminal jaringan beban. Jarum analog menjadi pembanding visual arus; pembebanan rangkaian tetap dihitung dari model DMM digital.</div>
      </div>

      <div class="card">
        <h3>4. CATAT DATA PENELITIAN</h3>
        <div class="btnrow">
          <button id="record" class="active">＋ Catat percobaan</button>
          <button id="exportCSV">⇩ Ekspor CSV</button>
        </div>
        <div class="btnrow"><button id="clearData" class="red">Hapus semua data</button></div>
        <div class="status" id="logStatus">Belum ada percobaan yang dicatat.</div>
        <div class="hint">Pencatatan utama hanya diterima saat mode A valid, sumber ON, sekring utuh, dan kedua probe terpasang benar. Gunakan tombol <b>Ekspor CSV</b> untuk mengunduh tabel hasil percobaan.</div>
      </div>
    </aside>
  </div>

  <div class="card">
    <h3>TABEL DATA PENELITIAN</h3>
    <div class="tableWrap"><table>
      <thead><tr><th>No.</th><th>Topologi</th><th>Vs (V)</th><th>R (Ω)</th><th>Req (Ω)</th><th>I ideal (A)</th><th>I model (A)</th><th>Rating fuse (A)</th></tr></thead>
      <tbody id="dataRows"><tr><td colspan="8">Belum ada data. Lakukan pengukuran lalu tekan Catat percobaan.</td></tr></tbody>
    </table></div>
  </div>
  <div class="footer">VIRTUAL ELECTRONICS RESEARCH LAB • Model DC resistif • Semua angka adalah simulasi, bukan pengganti alat ukur fisik.</div>
</div>

<script>
(function(){
  'use strict';
  const root = document.getElementById('veLab');
  const $ = (id) => root.querySelector('#'+id);
  const canvas = $('bench');
  const ctx = canvas.getContext('2d');
  const chart = $('chart');
  const cctx = chart.getContext('2d');
  const W=1200, H=760;

  const state = {
    topology:'series', mode:'A', sourceOn:true, voltage:12, fuseRating:1,
    fuseBlown:false, fuseStress:0, fuseTripThreshold:1.6,
    selected:1, nextId:4, resistors:[
      {id:1,R:100,x:560,y:300},
      {id:2,R:100,x:795,y:300},
      {id:3,R:100,x:1030,y:300}
    ],
    red:{x:355,y:300,connected:true,targetId:'A+'},
    black:{x:435,y:300,connected:true,targetId:'A-'},
    drag:null, records:[], lastFrame:performance.now(), lastUI:0,
    analogRange:1, analogAngle:Math.PI
  };

  const PHYS = {sourceR:0.10, wireR:0.02, fuseR:0.05, ammeterBurden:0.05, voltmeterInput:10000000};
  const clamp=(v,a,b)=>Math.max(a,Math.min(b,v));
  const fmtOhm=(v)=>v>=1000?(v/1000).toFixed(v>=10000?1:2)+' kΩ':v.toFixed(v<10?2:1)+' Ω';
  const fmtA=(v)=>Number.isFinite(v)?(v<1?v.toFixed(4):v.toFixed(3))+' A':'—';
  const fmtV=(v)=>Number.isFinite(v)?v.toFixed(3)+' V':'—';

  function selectedResistor(){return state.resistors.find(r=>r.id===state.selected)||state.resistors[0];}
  function getReq(){
    const rs=state.resistors.map(r=>Math.max(0.001,r.R));
    if(state.topology==='series') return rs.reduce((a,b)=>a+b,0);
    return 1/rs.reduce((a,b)=>a+1/b,0);
  }
  function layoutComponents(){
    const n=state.resistors.length;
    if(state.topology==='series'){
      const start=560, end=1030, step=n===1?0:(end-start)/(n-1);
      state.resistors.forEach((r,i)=>{r.x=start+i*step;r.y=300;});
    }else{
      const start=190, end=450, step=n===1?0:(end-start)/(n-1);
      state.resistors.forEach((r,i)=>{r.x=805;r.y=start+i*step;});
    }
    refreshAttachedProbes();
  }
  function loadTargets(){
    if(state.topology==='series'){
      const first=state.resistors[0], last=state.resistors[state.resistors.length-1];
      return [{x:first.x-35,y:first.y,id:'LOAD+'},{x:last.x+35,y:last.y,id:'LOAD-'}];
    }
    return [{x:555,y:300,id:'LOAD+'},{x:1080,y:300,id:'LOAD-'}];
  }
  function modeTargets(){
    if(state.mode==='A') return [{x:355,y:300,id:'A+'},{x:435,y:300,id:'A-'}];
    return loadTargets();
  }
  function probesReady(){
    const t=modeTargets();
    return state.red.connected && state.black.connected && state.red.targetId===t[0].id && state.black.targetId===t[1].id;
  }
  function refreshAttachedProbes(){
    const t=modeTargets();
    if(state.red.connected && state.red.targetId===t[0].id){state.red.x=t[0].x;state.red.y=t[0].y;}
    if(state.black.connected && state.black.targetId===t[1].id){state.black.x=t[1].x;state.black.y=t[1].y;}
  }
  function autoConnect(){
    const t=modeTargets();
    state.red={...state.red,x:t[0].x,y:t[0].y,connected:true,targetId:t[0].id};
    state.black={...state.black,x:t[1].x,y:t[1].y,connected:true,targetId:t[1].id};
  }
  function disconnectProbes(){
    state.red.connected=false;state.black.connected=false;
    state.red.targetId=null;state.black.targetId=null;
    state.red.x=650;state.red.y=535;state.black.x=730;state.black.y=535;
  }

  function electrical(){
    const Req=getReq();
    const fixed=PHYS.sourceR+PHYS.wireR+PHYS.fuseR;
    let Iloop=0,Vload=0,Iload=0,Ivm=0,openA=false,ReqEff=Req;
    if(state.sourceOn && !state.fuseBlown){
      if(state.mode==='A'){
        if(!probesReady()) openA=true;
        else{
          Iloop=state.voltage/(Req+fixed+PHYS.ammeterBurden);
          Vload=Iloop*Req;
          Iload=Iloop;
        }
      }else if(state.mode==='V' && probesReady()){
        ReqEff=1/(1/Req+1/PHYS.voltmeterInput);
        Iloop=state.voltage/(ReqEff+fixed);
        Vload=Iloop*ReqEff;
        Iload=Vload/Req;
        Ivm=Vload/PHYS.voltmeterInput;
      }else{
        Iloop=state.voltage/(Req+fixed);
        Vload=Iloop*Req;
        Iload=Iloop;
      }
    }
    let branches=[];
    if(state.topology==='series') branches=state.resistors.map(r=>({id:r.id,R:r.R,I:Iload,V:Iload*r.R}));
    else branches=state.resistors.map(r=>({id:r.id,R:r.R,I:Vload/r.R,V:Vload}));
    return {Req,ReqEff,Iloop,Vload,Iload,Ivm,branches,openA,idealI:state.voltage/Req};
  }

  function updateFuse(dt){
    if(!state.sourceOn || state.fuseBlown){return;}
    const e=electrical();
    if(e.Iloop>state.fuseRating){
      const normalized=e.Iloop/state.fuseRating;
      state.fuseStress += Math.max(0,normalized*normalized-1)*dt;
      if(state.fuseStress>=state.fuseTripThreshold){state.fuseBlown=true;state.fuseStress=0;}
    }else{
      state.fuseStress=Math.max(0,state.fuseStress-dt*0.35);
    }
  }

  function meterReadout(){
    const e=electrical();
    if(state.mode==='A'){
      if(!probesReady()) return {main:'OL',unit:'A',desc:'Amperemeter belum dimasukkan pada celah seri (A+ dan A−).'};
      return {main:e.Iloop.toFixed(4),unit:'A',desc:state.fuseBlown?'Sekring putus: arus rangkaian = 0 A.':(!state.sourceOn?'Sumber OFF: arus = 0 A.':'Pembacaan arus total dalam mode amperemeter seri.')};
    }
    if(state.mode==='V'){
      if(!probesReady()) return {main:'— — —',unit:'V',desc:'Voltmeter harus dipasang pada kedua terminal beban (paralel).'};
      return {main:e.Vload.toFixed(3),unit:'V',desc:'Pembacaan tegangan pada seluruh jaringan resistor.'};
    }
    if(state.sourceOn) return {main:'LIVE!',unit:'Ω',desc:'PENGUKURAN DITOLAK: matikan sumber sebelum memakai mode Ω.'};
    if(!probesReady()) return {main:'OL',unit:'Ω',desc:'Pasang probe pada kedua terminal jaringan beban.'};
    return {main:e.Req.toFixed(3),unit:'Ω',desc:'Hambatan ekuivalen jaringan resistor saat sumber OFF.'};
  }

  function rr(x,y,w,h,r,fill,stroke,lineWidth=2){
    ctx.beginPath();ctx.roundRect(x,y,w,h,r);
    if(fill){ctx.fillStyle=fill;ctx.fill();}
    if(stroke){ctx.strokeStyle=stroke;ctx.lineWidth=lineWidth;ctx.stroke();}
  }
  function txt(s,x,y,size,color='#e8f0f7',align='left',weight='normal'){
    ctx.fillStyle=color;ctx.font=weight+' '+size+'px Arial';ctx.textAlign=align;ctx.fillText(String(s),x,y);
  }
  function ln(x1,y1,x2,y2,color='#4bd8c6',width=3,dash=[]){
    ctx.beginPath();ctx.setLineDash(dash);ctx.moveTo(x1,y1);ctx.lineTo(x2,y2);ctx.strokeStyle=color;ctx.lineWidth=width;ctx.lineCap='round';ctx.stroke();ctx.setLineDash([]);
  }
  function wire(x1,y1,x2,y2,color='#4bd8c6',width=3){
    const mid=(x1+x2)/2;
    ctx.beginPath();ctx.moveTo(x1,y1);ctx.lineTo(mid,y1);ctx.lineTo(mid,y2);ctx.lineTo(x2,y2);
    ctx.strokeStyle=color;ctx.lineWidth=width;ctx.lineCap='round';ctx.lineJoin='round';ctx.stroke();
  }
  function dot(x,y,color='#d7e8f1',r=5){ctx.beginPath();ctx.arc(x,y,r,0,Math.PI*2);ctx.fillStyle=color;ctx.fill();}
  function formatCanvasOhm(v){return v>=1000?(v/1000).toFixed(1)+'kΩ':(v>=100?v.toFixed(0)+'Ω':v.toFixed(1)+'Ω');}

  function drawBackground(){
    const g=ctx.createLinearGradient(0,0,0,H);g.addColorStop(0,'#1b3044');g.addColorStop(1,'#101b29');ctx.fillStyle=g;ctx.fillRect(0,0,W,H);
    ctx.strokeStyle='rgba(180,215,235,.055)';ctx.lineWidth=1;
    for(let x=0;x<W;x+=30){ctx.beginPath();ctx.moveTo(x,0);ctx.lineTo(x,H);ctx.stroke();}
    for(let y=0;y<H;y+=30){ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(W,y);ctx.stroke();}
    rr(20,18,1160,510,14,'rgba(7,17,28,.18)','#304b61',1);
    txt('DC RESISTIVE CIRCUIT • DRAG RESISTORS / PROBES',600,43,15,'#56decf','center','bold');
  }
  function drawSource(){
    ln(165,300,165,326,'#4bd8c6',3);ln(165,430,165,455,'#4bd8c6',3);
    rr(65,326,100,104,12,'#263e53','#7895a9',2);
    ln(95,362,137,362,'#eaf4fa',4);ln(105,392,127,392,'#eaf4fa',2);
    txt('DC SOURCE',115,344,11,'#cce0eb','center','bold');
    txt(state.voltage.toFixed(1)+' V',115,414,17,'#62e7d5','center','bold');
    txt('+',174,305,16,'#ff7777','center','bold');txt('−',174,437,16,'#c9d7e1','center','bold');
    txt(state.sourceOn?'ON':'OFF',115,447,10,state.sourceOn?'#5ee3a1':'#ff9b76','center','bold');
  }
  function drawFuse(){
    ln(165,300,215,300,'#4bd8c6',3);ln(275,300,350,300,'#4bd8c6',3);
    rr(213,281,64,38,10,'#a4b4c0','#e2edf4',2);
    rr(221,286,48,28,9,'rgba(172,234,250,.25)','#d2f5ff',1.5);
    ln(226,300,state.fuseBlown?239:264,300,state.fuseBlown?'#f56a61':'#ffd77a',3);
    if(state.fuseBlown){ln(239,300,245,292,'#ff625c',3);ln(251,308,257,300,'#ff625c',3);dot(245,300,'rgba(255,90,80,.8)',7);}
    else {ln(264,300,269,300,'#ffd77a',3);}
    txt('FUSE',245,270,10,'#dbe8ef','center','bold');
    txt(state.fuseBlown?'BLOWN':state.fuseRating.toFixed(2)+' A',245,338,10,state.fuseBlown?'#ff8077':'#a9c2d2','center','bold');
    if(!state.fuseBlown){
      const p=clamp(state.fuseStress/state.fuseTripThreshold,0,1);
      rr(210,347,70,5,3,'#263a4c',null);rr(210,347,70*p,5,3,p>.7?'#f06c63':'#4cd7c4',null);
    }
  }
  function drawCurrentGap(){
    if(state.mode==='A'){
      ln(350,300,355,300,'#4bd8c6',3);ln(435,300,510,300,'#4bd8c6',3);
      if(probesReady()) ln(355,300,435,300,'#62e3ae',4);
      else {ln(355,300,377,300,'#f0b75d',3);ln(413,300,435,300,'#f0b75d',3);}
      dot(355,300,'#f8c75e',7);dot(435,300,'#f8c75e',7);
      txt('A+',355,282,10,'#ff8d8d','center','bold');txt('A−',435,282,10,'#c9d9e5','center','bold');
      txt('SERIES METER GAP',395,326,9,'#b9cbd8','center');
    }else{
      ln(350,300,510,300,'#4bd8c6',3);
    }
  }
  function drawResistor(r,index){
    const x=r.x,y=r.y,selected=r.id===state.selected;
    ln(x-44,y,x-34,y,'#9fb5c5',3);ln(x+34,y,x+44,y,'#9fb5c5',3);
    rr(x-34,y-15,68,30,5,selected?'#f8e7b5':'#dfd0a8',selected?'#4ce4cf':'#9aa9b5',selected?3:1.5);
    ctx.beginPath();ctx.moveTo(x-27,y);ctx.lineTo(x-19,y-8);ctx.lineTo(x-10,y+8);ctx.lineTo(x,y-8);ctx.lineTo(x+10,y+8);ctx.lineTo(x+19,y-8);ctx.lineTo(x+27,y);ctx.strokeStyle='#49576a';ctx.lineWidth=2.5;ctx.stroke();
    txt('R'+(index+1)+'  '+formatCanvasOhm(r.R),x,y+31,10,selected?'#73eadc':'#cad9e3','center','bold');
    if(selected){ctx.beginPath();ctx.arc(x,y,43,0,Math.PI*2);ctx.strokeStyle='rgba(76,224,201,.65)';ctx.lineWidth=1.5;ctx.setLineDash([4,4]);ctx.stroke();ctx.setLineDash([]);}
  }
  function drawSeries(){
    const rs=state.resistors;
    const first=rs[0],last=rs[rs.length-1];
    wire(510,300,first.x-44,first.y);
    for(let i=0;i<rs.length-1;i++) wire(rs[i].x+44,rs[i].y,rs[i+1].x-44,rs[i+1].y);
    wire(last.x+44,last.y,1100,300);
    rs.forEach(drawResistor);
  }
  function drawParallel(){
    const left=555,right=1080;
    const ys=state.resistors.map(r=>r.y);
    const top=Math.min(170,...ys)-10,bottom=Math.max(470,...ys)+10;
    ln(left,top,left,bottom,'#4bd8c6',4);ln(right,top,right,bottom,'#4bd8c6',4);
    ln(510,300,left,300,'#4bd8c6',3);ln(right,300,1100,300,'#4bd8c6',3);
    state.resistors.forEach((r,i)=>{
      ln(left,r.y,r.x-44,r.y,'#4bd8c6',2.5);ln(r.x+44,r.y,right,r.y,'#4bd8c6',2.5);
      drawResistor(r,i);
    });
  }
  function drawReturn(){
    ln(1100,300,1100,485,'#4bd8c6',3);ln(1100,485,165,485,'#4bd8c6',3);ln(165,485,165,455,'#4bd8c6',3);
    dot(165,300,'#69e6d5',5);dot(165,455,'#69e6d5',5);
  }
  function drawTargets(){
    const t=modeTargets();
    const labels=state.mode==='A'?['A+','A−']:(state.mode==='V'?['V+','V−']:['Ω+','Ω−']);
    t.forEach((p,i)=>{
      ctx.beginPath();ctx.arc(p.x,p.y,11,0,Math.PI*2);ctx.fillStyle='rgba(69,226,203,.15)';ctx.fill();ctx.strokeStyle='#67ead7';ctx.lineWidth=2;ctx.stroke();
      txt(labels[i],p.x,p.y-16,10,'#91f2e6','center','bold');
    });
  }
  function drawProbe(p,type){
    const red=type==='red', color=red?'#f04444':'#1a2634';
    const sx=red?845:925, sy=706;
    ctx.beginPath();ctx.moveTo(sx,sy);ctx.bezierCurveTo(sx-50,sy-70,p.x+(red?-65:65),p.y+95,p.x,p.y);
    ctx.strokeStyle=color;ctx.lineWidth=5;ctx.lineCap='round';ctx.stroke();
    ctx.save();ctx.translate(p.x,p.y);ctx.rotate(-Math.PI/4);
    rr(-8,-30,16,36,5,color,'#bdcbd5',1.5);rr(-4,-42,8,16,2,'#b9c8d2','#eef5f8',1);
    ctx.restore();dot(p.x,p.y,red?'#ffd5d5':'#d9e3eb',4);
    txt(red?'+':'−',p.x,p.y-34,13,'#ffffff','center','bold');
    if(p.connected) dot(p.x,p.y,red?'#ff7777':'#8bc3da',8);
  }
  function drawAnalogMeter(){
    rr(35,548,420,190,20,'#263b50','#7793a7',2);
    txt('ANALOG AMMETER • PEMBANDING ARUS',245,573,12,'#dce8f0','center','bold');
    const cx=245,cy=690,rad=83;
    ctx.beginPath();ctx.arc(cx,cy,rad,Math.PI,0,false);ctx.strokeStyle='#e5edf2';ctx.lineWidth=3;ctx.stroke();
    const e=electrical();
    const usable=state.mode==='A';
    const val=usable?e.Iload:0;
    const target=Math.PI-clamp(val/state.analogRange,0,1)*Math.PI;
    state.analogAngle+=(target-state.analogAngle)*0.14;
    for(let i=0;i<=5;i++){
      const a=Math.PI-i*Math.PI/5;
      const x1=cx+(rad-7)*Math.cos(a),y1=cy-(rad-7)*Math.sin(a);
      const x2=cx+(rad+3)*Math.cos(a),y2=cy-(rad+3)*Math.sin(a);
      ln(x1,y1,x2,y2,'#e5edf2',2);
      const tx=cx+(rad+18)*Math.cos(a),ty=cy-(rad+18)*Math.sin(a);
      txt((state.analogRange*i/5).toFixed(state.analogRange<1?2:1),tx,ty+4,9,'#dce8f0','center');
    }
    const nx=cx+(rad-17)*Math.cos(state.analogAngle),ny=cy-(rad-17)*Math.sin(state.analogAngle);
    ln(cx,cy,nx,ny,'#ff5d5d',4);dot(cx,cy,'#e8eef3',8);
    txt(usable?fmtA(val):'PILIH MODE A',245,730,11,usable?'#71e8d1':'#f0bf72','center','bold');
    if(usable && val>state.analogRange) txt('OVER RANGE',245,590,9,'#ff7777','center','bold');
    else txt('SKALA ARUS',245,590,9,'#a8bdcc','center');
  }

  function drawDMM(){
    rr(770,548,390,190,20,'#263b50','#7793a7',2);
    rr(790,566,205,75,8,'#91b49b','#d6f1d9',2);
    const reading=meterReadout();
    txt(reading.main,892,612,31,'#102b23','center','bold');
    txt(reading.unit,974,630,12,'#173c2b','center','bold');
    txt('DIGITAL MULTIMETER',892,657,10,'#dce8f0','center','bold');
    const cx=1070,cy=625;
    ctx.beginPath();ctx.arc(cx,cy,43,0,Math.PI*2);ctx.fillStyle='#101e2b';ctx.fill();ctx.strokeStyle='#a7bac8';ctx.lineWidth=2;ctx.stroke();
    ctx.beginPath();ctx.arc(cx,cy,30,0,Math.PI*2);ctx.fillStyle='#516a7c';ctx.fill();
    const a=state.mode==='A'?-2.3:(state.mode==='V'?-0.2:2.3);
    ln(cx,cy,cx+25*Math.cos(a),cy+25*Math.sin(a),'#f5f7f8',6);dot(cx,cy,'#d9e3ea',7);
    txt('A',1029,576,11,'#fff','center','bold');txt('V',1113,576,11,'#fff','center','bold');txt('Ω',1115,676,12,'#fff','center','bold');
    txt('KLIK KNOB',1070,694,9,'#b6c8d5','center');
    dot(845,706,'#f04444',10);dot(925,706,'#101827',10);
    txt('VΩ / A',845,727,9,'#edf5f8','center');txt('COM',925,727,9,'#edf5f8','center');
    txt(state.mode==='A'?'AMMETER • SERIES':state.mode==='V'?'VOLTMETER • PARALLEL':'OHMMETER • SOURCE OFF',892,682,9,'#9fbbc9','center','bold');
  }
  function draw(){
    ctx.clearRect(0,0,W,H);drawBackground();drawSource();drawFuse();drawCurrentGap();
    if(state.topology==='series') drawSeries(); else drawParallel();
    drawReturn();drawTargets();drawAnalogMeter();drawDMM();drawProbe(state.red,'red');drawProbe(state.black,'black');
    txt(state.topology==='series'?'TOPOLOGI SERI':'TOPOLOGI PARALEL',590,80,12,'#9ddbd4','center','bold');
    txt('Sekring dipasang seri dengan sumber dan seluruh jaringan beban.',600,505,10,'#a8bdcc','center');
  }

  function updatePanel(){
    const e=electrical(),m=meterReadout();
    $('mReq').textContent=fmtOhm(e.Req);
    $('mI').textContent=fmtA(e.Iload);
    $('mIdeal').textContent=fmtA(e.idealI);
    $('mVload').textContent=fmtV(e.Vload);
    $('mMeter').textContent=m.main+' '+m.unit;
    $('mFuse').textContent=state.fuseBlown?'PUTUS':(state.fuseStress>0?'BEBAN LEBIH':'UTUH');
    $('mFuse').style.color=state.fuseBlown?'#ff7777':(state.fuseStress>0?'#f3c477':'#65e2ad');
    const b=e.branches.map((v,i)=>'R'+(i+1)+': '+fmtA(v.I)+'  |  V'+(i+1)+': '+fmtV(v.V));
    $('branchInfo').textContent='Arus / tegangan tiap resistor:\n'+b.join('\n')+'\nΣ arus cabang paralel = '+fmtA(e.branches.reduce((s,v)=>s+v.I,0));
    const status=$('measurementStatus');
    status.textContent=m.desc+'  '+(state.fuseBlown?'Sekring telah putus; tekan Reset sekring untuk memulihkan.':state.fuseStress>0?'Stres termal sekring: '+(100*state.fuseStress/state.fuseTripThreshold).toFixed(0)+'%.':'');
    status.className='status'+(state.fuseBlown?' bad':(state.mode==='Ω'&&state.sourceOn?' warn':''));
    $('selectedName').textContent='R'+(state.resistors.findIndex(r=>r.id===state.selected)+1);
    const sr=selectedResistor();
    $('rValue').textContent=fmtOhm(sr.R);
    $('rSlider').value=String(clamp(Math.round(Math.log10(sr.R)*100),0,400));
    $('voltageValue').textContent=state.voltage.toFixed(1)+' V';
    $('fuseRating').value=String(state.fuseRating);
    $('sourceToggle').textContent=state.sourceOn?'Sumber ON':'Sumber OFF';
    $('sourceToggle').classList.toggle('active',state.sourceOn);
    $('topSeries').classList.toggle('active',state.topology==='series');
    $('topParallel').classList.toggle('active',state.topology==='parallel');
    $('modeA').classList.toggle('active',state.mode==='A');
    $('modeV').classList.toggle('active',state.mode==='V');
    $('modeOhm').classList.toggle('active',state.mode==='Ω');
    $('addR').disabled=state.resistors.length>=8;
    $('removeR').disabled=state.resistors.length<=1;
  }
  function renderTable(){
    const body=$('dataRows');
    if(!state.records.length){body.innerHTML='<tr><td colspan="8">Belum ada data. Lakukan pengukuran lalu tekan Catat percobaan.</td></tr>';return;}
    body.innerHTML=state.records.map((r,i)=>'<tr><td>'+(i+1)+'</td><td>'+r.topology+'</td><td>'+r.voltage_V.toFixed(2)+'</td><td>'+r.resistors_ohm.map(v=>Number(v.toPrecision(4))).join(' ; ')+'</td><td>'+r.Req_ohm.toFixed(4)+'</td><td>'+r.I_ideal_A.toFixed(5)+'</td><td>'+r.I_model_A.toFixed(5)+'</td><td>'+r.fuse_rating_A+'</td></tr>').join('');
  }
  function drawChart(){
    const w=chart.width,h=chart.height;cctx.clearRect(0,0,w,h);cctx.fillStyle='#0c1926';cctx.fillRect(0,0,w,h);
    const L=72,R=25,T=25,B=55,pw=w-L-R,ph=h-T-B;
    cctx.strokeStyle='#35536a';cctx.lineWidth=1;
    for(let i=0;i<=5;i++){let y=T+ph*i/5;cctx.beginPath();cctx.moveTo(L,y);cctx.lineTo(L+pw,y);cctx.stroke();}
    cctx.beginPath();cctx.moveTo(L,T);cctx.lineTo(L,T+ph);cctx.lineTo(L+pw,T+ph);cctx.strokeStyle='#8da7b8';cctx.stroke();
    cctx.fillStyle='#c2d2de';cctx.font='12px Arial';cctx.textAlign='center';cctx.fillText('Hambatan ekuivalen Req (Ω) • log',L+pw/2,h-13);
    cctx.save();cctx.translate(18,T+ph/2);cctx.rotate(-Math.PI/2);cctx.fillText('Arus total model (A)',0,0);cctx.restore();
    if(!state.records.length){cctx.fillStyle='#8fa9ba';cctx.font='15px Arial';cctx.fillText('Catat percobaan untuk membentuk grafik',w/2,h/2);return;}
    const minR=Math.min(...state.records.map(d=>d.Req_ohm)),maxR=Math.max(...state.records.map(d=>d.Req_ohm));
    const xMin=Math.log10(Math.max(.1,minR*.8)),xMax=Math.log10(Math.max(minR*1.2,maxR*1.25));
    const maxI=Math.max(...state.records.map(d=>d.I_model_A),.001)*1.2;
    const X=v=>L+(Math.log10(Math.max(.1,v))-xMin)/(xMax-xMin||1)*pw;
    const Y=v=>T+ph-(v/maxI)*ph;
    for(let i=0;i<=5;i++){let val=maxI*i/5;cctx.fillStyle='#a9bdca';cctx.font='10px Arial';cctx.textAlign='right';cctx.fillText(val.toFixed(3),L-8,Y(val)+3);}
    state.records.forEach(d=>{
      const color=d.topology==='Seri'?'#46d8c4':'#ffb45e';
      cctx.beginPath();cctx.arc(X(d.Req_ohm),Y(d.I_model_A),6,0,Math.PI*2);cctx.fillStyle=color;cctx.fill();cctx.strokeStyle='#f4f7f9';cctx.lineWidth=1;cctx.stroke();
    });
    cctx.font='11px Arial';cctx.textAlign='left';cctx.fillStyle='#46d8c4';cctx.fillText('● Seri',L+8,T+13);cctx.fillStyle='#ffb45e';cctx.fillText('● Paralel',L+85,T+13);
  }
  function refresh(){draw();updatePanel();drawChart();}

  function pointerPos(ev){const r=canvas.getBoundingClientRect();return {x:(ev.clientX-r.left)*W/r.width,y:(ev.clientY-r.top)*H/r.height};}
  function dist(a,b){return Math.hypot(a.x-b.x,a.y-b.y);}
  function findResistor(p){for(let i=state.resistors.length-1;i>=0;i--){const r=state.resistors[i];if(Math.abs(p.x-r.x)<43&&Math.abs(p.y-r.y)<25)return r;}return null;}
  canvas.addEventListener('pointerdown',ev=>{
    const p=pointerPos(ev);
    if(dist(p,{x:1070,y:625})<46){setMode(state.mode==='A'?'V':state.mode==='V'?'Ω':'A');ev.preventDefault();return;}
    if(dist(p,state.red)<27){state.drag='red';canvas.setPointerCapture(ev.pointerId);return;}
    if(dist(p,state.black)<27){state.drag='black';canvas.setPointerCapture(ev.pointerId);return;}
    const r=findResistor(p);
    if(r){state.selected=r.id;state.drag='resistor';canvas.setPointerCapture(ev.pointerId);refresh();return;}
  });
  canvas.addEventListener('pointermove',ev=>{
    if(!state.drag)return;const p=pointerPos(ev);
    if(state.drag==='red'||state.drag==='black'){
      const q=state[state.drag];q.x=p.x;q.y=p.y;q.connected=false;q.targetId=null;
    }else if(state.drag==='resistor'){
      const r=selectedResistor();
      if(state.topology==='series') r.y=clamp(p.y,205,415);
      else {const idx=state.resistors.indexOf(r);const lane=state.resistors.length===1?320:190+idx*260/(state.resistors.length-1);r.x=clamp(p.x,650,985);r.y=clamp(p.y,lane-9,lane+9);}
      refreshAttachedProbes();
    }
  });
  function finishPointer(){
    if(state.drag==='red'||state.drag==='black'){
      const role=state.drag;const p=state[role];const targets=modeTargets();const expected=role==='red'?targets[0]:targets[1];
      if(dist(p,expected)<42){p.x=expected.x;p.y=expected.y;p.connected=true;p.targetId=expected.id;}
      else {p.connected=false;p.targetId=null;}
    }
    state.drag=null;refresh();
  }
  canvas.addEventListener('pointerup',finishPointer);canvas.addEventListener('pointercancel',finishPointer);

  function setMode(m){state.mode=m;state.red.connected=false;state.black.connected=false;state.red.targetId=null;state.black.targetId=null;refresh();}
  function setTopology(t){state.topology=t;layoutComponents();refresh();}
  $('topSeries').onclick=()=>setTopology('series');
  $('topParallel').onclick=()=>setTopology('parallel');
  $('addR').onclick=()=>{
    if(state.resistors.length>=8)return;
    const r={id:state.nextId++,R:100,x:800,y:300};state.resistors.push(r);state.selected=r.id;layoutComponents();refresh();
  };
  $('removeR').onclick=()=>{
    if(state.resistors.length<=1)return;
    const ix=state.resistors.findIndex(r=>r.id===state.selected);state.resistors.splice(ix,1);state.selected=state.resistors[Math.max(0,ix-1)].id;layoutComponents();refresh();
  };
  $('resetLayout').onclick=()=>{layoutComponents();refresh();};
  $('rSlider').addEventListener('input',ev=>{
    const r=selectedResistor();r.R=Math.pow(10,Number(ev.target.value)/100);$('rValue').textContent=fmtOhm(r.R);refresh();
  });
  root.querySelectorAll('[data-r]').forEach(btn=>btn.addEventListener('click',()=>{
    const r=selectedResistor();r.R=Number(btn.dataset.r);$('rSlider').value=String(Math.round(Math.log10(r.R)*100));refresh();
  }));
  $('voltageSlider').addEventListener('input',ev=>{state.voltage=Number(ev.target.value);refresh();});
  $('fuseRating').addEventListener('change',ev=>{state.fuseRating=Number(ev.target.value);state.fuseStress=0;refresh();});
  $('sourceToggle').onclick=()=>{state.sourceOn=!state.sourceOn;refresh();};
  $('resetFuse').onclick=()=>{state.fuseBlown=false;state.fuseStress=0;refresh();};
  $('modeA').onclick=()=>setMode('A');$('modeV').onclick=()=>setMode('V');$('modeOhm').onclick=()=>setMode('Ω');
  $('analogRange').addEventListener('change',ev=>{state.analogRange=Number(ev.target.value);refresh();});
  $('autoConnect').onclick=()=>{autoConnect();refresh();};
  $('disconnect').onclick=()=>{disconnectProbes();refresh();};

  function recordTrial(){
    const e=electrical();
    if(state.mode!=='A'){ $('logStatus').textContent='Pilih mode A dan ukur arus dengan probe dipasang seri untuk mencatat arus total.';return; }
    if(!probesReady()){ $('logStatus').textContent='Belum valid: hubungkan probe merah ke A+ dan hitam ke A−.';return; }
    if(!state.sourceOn){ $('logStatus').textContent='Sumber OFF. Nyalakan sumber untuk pengukuran arus.';return; }
    if(state.fuseBlown){ $('logStatus').textContent='Sekring putus. Reset sekring sebelum mencatat percobaan baru.';return; }
    const record={
      trial:state.records.length+1,
      topology:state.topology==='series'?'Seri':'Paralel',
      voltage_V:state.voltage,
      resistor_count:state.resistors.length,
      resistors_ohm:state.resistors.map(r=>Number(r.R.toFixed(6))),
      Req_ohm:Number(e.Req.toFixed(8)),
      I_ideal_A:Number(e.idealI.toFixed(10)),
      I_model_A:Number(e.Iloop.toFixed(10)),
      V_load_V:Number(e.Vload.toFixed(8)),
      branch_currents_A:e.branches.map(b=>Number(b.I.toFixed(10))),
      fuse_rating_A:state.fuseRating,
      fuse_status:state.fuseBlown?'PUTUS':'UTUH'
    };
    state.records.push(record);renderTable();drawChart();
    $('logStatus').textContent='Percobaan '+record.trial+' tersimpan di tabel. Gunakan tombol Ekspor CSV untuk mengunduh data.';
  }
  $('record').onclick=recordTrial;
  $('clearData').onclick=()=>{state.records=[];renderTable();drawChart();$('logStatus').textContent='Data percobaan dihapus.';};
  $('exportCSV').onclick=()=>{
    if(!state.records.length){$('logStatus').textContent='Belum ada data untuk diekspor.';return;}
    const headers=['trial','topology','voltage_V','resistor_count','resistors_ohm','Req_ohm','I_ideal_A','I_model_A','V_load_V','branch_currents_A','fuse_rating_A','fuse_status'];
    const csv=[headers.join(','),...state.records.map(r=>headers.map(k=>{
      const v=Array.isArray(r[k])?r[k].join('; '):r[k];return '"'+String(v??'').replace(/"/g,'""')+'"';
    }).join(','))].join('\n');
    const blob=new Blob(['\uFEFF'+csv],{type:'text/csv;charset=utf-8;'});const url=URL.createObjectURL(blob);const a=document.createElement('a');a.href=url;a.download='data_penelitian_resistor_seri_paralel.csv';document.body.appendChild(a);a.click();a.remove();URL.revokeObjectURL(url);
    $('logStatus').textContent='CSV berhasil diunduh.';
  };

  function frame(now){
    const dt=Math.min(.05,Math.max(0,(now-state.lastFrame)/1000));state.lastFrame=now;
    updateFuse(dt);
    draw();
    if(now-state.lastUI>180){updatePanel();state.lastUI=now;}
    requestAnimationFrame(frame);
  }

  layoutComponents();autoConnect();renderTable();refresh();requestAnimationFrame(frame);
})();
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    app.run()