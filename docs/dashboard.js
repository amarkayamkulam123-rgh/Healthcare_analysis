/* ═══════════════════════════════════════════════
   Healthcare BI Dashboard — JavaScript Engine
   ═══════════════════════════════════════════════ */

// ── Chart.js Global Defaults ──
Chart.defaults.color = '#8FA3B8';
Chart.defaults.borderColor = '#162D45';
Chart.defaults.font.family = "'Inter', sans-serif";
Chart.defaults.font.size = 11;
Chart.defaults.plugins.legend.labels.usePointStyle = true;
Chart.defaults.plugins.legend.labels.pointStyle = 'circle';
Chart.defaults.plugins.legend.labels.padding = 16;
Chart.defaults.plugins.tooltip.backgroundColor = 'rgba(15, 34, 55, 0.95)';
Chart.defaults.plugins.tooltip.borderColor = '#1A3A5C';
Chart.defaults.plugins.tooltip.borderWidth = 1;
Chart.defaults.plugins.tooltip.titleColor = '#E0E7EF';
Chart.defaults.plugins.tooltip.bodyColor = '#CBD5E1';
Chart.defaults.plugins.tooltip.padding = 12;
Chart.defaults.plugins.tooltip.cornerRadius = 10;
Chart.defaults.plugins.tooltip.displayColors = true;
Chart.defaults.animation.duration = 800;
Chart.defaults.animation.easing = 'easeOutQuart';

// ── Color Palette ──
const COLORS = {
    teal: '#00BFA5',
    purple: '#7C4DFF',
    orange: '#FF6D00',
    blue: '#00B0FF',
    pink: '#FF4081',
    yellow: '#FFAB00',
    green: '#64DD17',
    magenta: '#D500F9',
    mint: '#1DE9B6',
    red: '#F50057',
    cyan: '#00E5FF',
    gold: '#FFD740',
};

const CHART_COLORS = [
    COLORS.teal, COLORS.purple, COLORS.orange, COLORS.blue,
    COLORS.pink, COLORS.yellow, COLORS.green, COLORS.magenta,
    COLORS.mint, COLORS.red, COLORS.cyan, COLORS.gold,
];

const CHART_COLORS_ALPHA = CHART_COLORS.map(c => c + '33');

// ── Utility Functions ──
function formatCurrency(val) {
    if (val >= 1e9) return '$' + (val / 1e9).toFixed(2) + 'B';
    if (val >= 1e6) return '$' + (val / 1e6).toFixed(1) + 'M';
    if (val >= 1e3) return '$' + (val / 1e3).toFixed(1) + 'K';
    return '$' + val.toFixed(2);
}

function formatNumber(val) {
    return val.toLocaleString('en-US');
}

function createGradient(ctx, colorStart, colorEnd) {
    const gradient = ctx.createLinearGradient(0, 0, 0, ctx.canvas.height);
    gradient.addColorStop(0, colorStart);
    gradient.addColorStop(1, colorEnd);
    return gradient;
}

// ── Chart Instance Storage ──
const chartInstances = {};

function destroyChart(id) {
    if (chartInstances[id]) {
        chartInstances[id].destroy();
        delete chartInstances[id];
    }
}

// ── Navigation ──
const pages = {
    overview: { title: 'Executive Overview' },
    demographics: { title: 'Patient Demographics' },
    clinical: { title: 'Clinical Analysis' },
    billing: { title: 'Billing & Revenue' },
};

let currentPage = 'overview';

function switchPage(pageName) {
    if (!pages[pageName]) return;

    // Update nav
    document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.toggle('active', link.dataset.page === pageName);
    });

    // Update pages
    document.querySelectorAll('.page').forEach(page => {
        page.classList.remove('active');
    });
    document.getElementById('page-' + pageName).classList.add('active');

    // Update title
    document.getElementById('page-title').textContent = pages[pageName].title;

    currentPage = pageName;

    // Close mobile sidebar
    document.getElementById('sidebar').classList.remove('open');
    const overlay = document.querySelector('.sidebar-overlay');
    if (overlay) overlay.classList.remove('show');
}

// ── Sidebar Toggle ──
document.getElementById('sidebar-toggle').addEventListener('click', () => {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('open');
    let overlay = document.querySelector('.sidebar-overlay');
    if (!overlay) {
        overlay = document.createElement('div');
        overlay.className = 'sidebar-overlay';
        document.body.appendChild(overlay);
        overlay.addEventListener('click', () => {
            sidebar.classList.remove('open');
            overlay.classList.remove('show');
        });
    }
    overlay.classList.toggle('show');
});

// Nav link click handlers
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        switchPage(link.dataset.page);
    });
});

// ── Counter Animation ──
function animateValue(el, end, prefix = '', suffix = '', decimals = 0) {
    const duration = 1200;
    const start = 0;
    const startTime = performance.now();

    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 4);
        const current = start + (end - start) * eased;

        if (decimals > 0) {
            el.textContent = prefix + current.toFixed(decimals) + suffix;
        } else {
            el.textContent = prefix + Math.floor(current).toLocaleString('en-US') + suffix;
        }

        if (progress < 1) {
            requestAnimationFrame(update);
        }
    }

    el.classList.add('counter-animate');
    requestAnimationFrame(update);
}

// ═══════════════════════════════════════
// CHART BUILDERS
// ═══════════════════════════════════════

function buildLineChart(canvasId, data, yPrefix = '') {
    destroyChart(canvasId);
    const ctx = document.getElementById(canvasId).getContext('2d');
    const gradient = createGradient(ctx, 'rgba(0, 191, 165, 0.25)', 'rgba(0, 191, 165, 0.01)');

    chartInstances[canvasId] = new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.labels,
            datasets: [{
                label: 'Value',
                data: data.values,
                borderColor: COLORS.teal,
                backgroundColor: gradient,
                borderWidth: 3,
                fill: true,
                tension: 0.4,
                pointRadius: 5,
                pointBackgroundColor: COLORS.teal,
                pointBorderColor: '#0F2237',
                pointBorderWidth: 2,
                pointHoverRadius: 8,
                pointHoverBorderWidth: 3,
            }],
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false },
                tooltip: {
                    callbacks: {
                        label: (ctx) => yPrefix + ctx.parsed.y.toLocaleString('en-US'),
                    },
                },
            },
            scales: {
                x: {
                    grid: { display: false },
                    ticks: { color: '#8FA3B8' },
                },
                y: {
                    grid: {
                        color: '#162D45',
                        drawBorder: false,
                        borderDash: [4, 4],
                    },
                    ticks: {
                        color: '#8FA3B8',
                        callback: (val) => yPrefix + (val >= 1e6 ? (val / 1e6).toFixed(1) + 'M' : val >= 1e3 ? (val / 1e3).toFixed(0) + 'K' : val),
                    },
                },
            },
        },
    });
}

function buildBarChart(canvasId, data, horizontal = false, colorIndex = 0, yPrefix = '') {
    destroyChart(canvasId);
    const ctx = document.getElementById(canvasId).getContext('2d');
    const colors = data.labels.map((_, i) => CHART_COLORS[(i + colorIndex) % CHART_COLORS.length]);
    const colorsAlpha = colors.map(c => c + '33');

    chartInstances[canvasId] = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.labels,
            datasets: [{
                data: data.values,
                backgroundColor: colors.map(c => c + 'CC'),
                borderColor: colors,
                borderWidth: 1,
                borderRadius: 6,
                borderSkipped: false,
            }],
        },
        options: {
            indexAxis: horizontal ? 'y' : 'x',
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false },
                tooltip: {
                    callbacks: {
                        label: (ctx) => yPrefix + ctx.parsed[horizontal ? 'x' : 'y'].toLocaleString('en-US'),
                    },
                },
            },
            scales: {
                x: {
                    grid: horizontal ? { color: '#162D45', borderDash: [4, 4] } : { display: false },
                    ticks: {
                        color: '#8FA3B8',
                        callback: function(val) {
                            if (horizontal && yPrefix) return yPrefix + (val >= 1e6 ? (val/1e6).toFixed(1)+'M' : val >= 1e3 ? (val/1e3).toFixed(0)+'K' : val);
                            return val;
                        }
                    },
                },
                y: {
                    grid: horizontal ? { display: false } : { color: '#162D45', borderDash: [4, 4] },
                    ticks: {
                        color: '#8FA3B8',
                        callback: function(val) {
                            if (!horizontal && yPrefix) return yPrefix + (val >= 1e6 ? (val/1e6).toFixed(1)+'M' : val >= 1e3 ? (val/1e3).toFixed(0)+'K' : val);
                            return this.getLabelForValue(val);
                        }
                    },
                },
            },
        },
    });
}

function buildDoughnutChart(canvasId, data, colorOffset = 0) {
    destroyChart(canvasId);
    const ctx = document.getElementById(canvasId).getContext('2d');
    const colors = data.labels.map((_, i) => CHART_COLORS[(i + colorOffset) % CHART_COLORS.length]);

    chartInstances[canvasId] = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: data.labels,
            datasets: [{
                data: data.values,
                backgroundColor: colors.map(c => c + 'DD'),
                borderColor: '#0F2237',
                borderWidth: 3,
                hoverBorderColor: '#1A3A5C',
                hoverOffset: 8,
            }],
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '65%',
            plugins: {
                legend: {
                    position: 'right',
                    labels: {
                        color: '#8FA3B8',
                        padding: 14,
                        font: { size: 11 },
                    },
                },
                tooltip: {
                    callbacks: {
                        label: (ctx) => {
                            const total = ctx.dataset.data.reduce((a, b) => a + b, 0);
                            const pct = ((ctx.parsed / total) * 100).toFixed(1);
                            return `${ctx.label}: ${ctx.parsed.toLocaleString()} (${pct}%)`;
                        },
                    },
                },
            },
        },
    });
}

function buildStackedBarChart(canvasId, data) {
    destroyChart(canvasId);
    const ctx = document.getElementById(canvasId).getContext('2d');

    chartInstances[canvasId] = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.labels,
            datasets: [
                {
                    label: 'Male',
                    data: data.male,
                    backgroundColor: COLORS.blue + 'CC',
                    borderColor: COLORS.blue,
                    borderWidth: 1,
                    borderRadius: 4,
                },
                {
                    label: 'Female',
                    data: data.female,
                    backgroundColor: COLORS.pink + 'CC',
                    borderColor: COLORS.pink,
                    borderWidth: 1,
                    borderRadius: 4,
                },
            ],
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'top',
                    labels: { color: '#8FA3B8' },
                },
            },
            scales: {
                x: {
                    stacked: true,
                    grid: { display: false },
                    ticks: { color: '#8FA3B8' },
                },
                y: {
                    stacked: true,
                    grid: { color: '#162D45', borderDash: [4, 4] },
                    ticks: { color: '#8FA3B8' },
                },
            },
        },
    });
}

function buildHeatmap(containerId, data) {
    const container = document.getElementById(containerId);
    const { conditions, testResults, values } = data;

    // Find max for color scaling
    const flat = values.flat();
    const maxVal = Math.max(...flat);
    const minVal = Math.min(...flat);

    function getHeatColor(val) {
        const ratio = (val - minVal) / (maxVal - minVal || 1);
        const r = Math.round(15 + ratio * (0 - 15));
        const g = Math.round(34 + ratio * (191 - 34));
        const b = Math.round(55 + ratio * (165 - 55));
        return `rgb(${r}, ${g}, ${b})`;
    }

    function getTextColor(val) {
        const ratio = (val - minVal) / (maxVal - minVal || 1);
        return ratio > 0.5 ? '#FFFFFF' : '#CBD5E1';
    }

    let html = '<table class="heatmap-table"><thead><tr><th>Medical Condition</th>';
    testResults.forEach(tr => { html += `<th>${tr}</th>`; });
    html += '</tr></thead><tbody>';

    conditions.forEach((cond, i) => {
        html += `<tr><td>${cond}</td>`;
        testResults.forEach((_, j) => {
            const val = values[i][j];
            html += `<td style="background:${getHeatColor(val)};color:${getTextColor(val)}">${val.toLocaleString()}</td>`;
        });
        html += '</tr>';
    });

    html += '</tbody></table>';
    container.innerHTML = html;
}

// ═══════════════════════════════════════
// DASHBOARD DATA LOADER
// ═══════════════════════════════════════

async function loadDashboard() {
    try {
        const resp = await fetch('dashboard_data.json');
        if (!resp.ok) throw new Error('Failed to load data');
        const D = await resp.json();

        // ── PAGE 1: Executive Overview ──
        animateValue(document.getElementById('val-revenue'), D.kpis.totalRevenue, '$', '', 0);
        animateValue(document.getElementById('val-patients'), D.kpis.totalPatients);
        animateValue(document.getElementById('val-hospitals'), D.kpis.totalHospitals);
        animateValue(document.getElementById('val-maxbill'), D.kpis.maxBilling, '$', '', 0);
        animateValue(document.getElementById('val-avgbill'), D.kpis.avgBilling, '$', '', 0);
        animateValue(document.getElementById('val-avgage'), D.kpis.avgAge, '', ' yrs', 1);
        animateValue(document.getElementById('val-male'), D.kpis.malePercent, '', '%', 1);
        animateValue(document.getElementById('val-female'), D.kpis.femalePercent, '', '%', 1);
        animateValue(document.getElementById('val-emergency'), D.kpis.emergencyPercent, '', '%', 1);
        animateValue(document.getElementById('val-avglos'), D.kpis.avgLOS, '', ' days', 1);

        buildLineChart('chart-revenue-year', D.revenueByYear, '$');
        buildDoughnutChart('chart-patients-condition', D.patientsByCondition);
        buildBarChart('chart-patients-month', D.patientsByMonth, false, 0);

        // ── PAGE 2: Patient Demographics ──
        animateValue(document.getElementById('val-patients-2'), D.kpis.totalPatients);
        animateValue(document.getElementById('val-avgage-2'), D.kpis.avgAge, '', ' yrs', 1);
        animateValue(document.getElementById('val-male-2'), D.kpis.malePercent, '', '%', 1);
        animateValue(document.getElementById('val-female-2'), D.kpis.femalePercent, '', '%', 1);

        buildBarChart('chart-age-group', D.patientsByAgeGroup, true, 0);
        buildDoughnutChart('chart-gender', D.genderDistribution, 3);
        buildStackedBarChart('chart-gender-age', D.genderByAgeGroup);
        buildBarChart('chart-blood-type', D.patientsByBloodType, false, 2);
        buildBarChart('chart-insurance', D.patientsByInsurance, true, 4);

        // ── PAGE 3: Clinical Analysis ──
        animateValue(document.getElementById('val-patients-3'), D.kpis.totalPatients);
        animateValue(document.getElementById('val-emergency-3'), D.kpis.emergencyPercent, '', '%', 1);
        animateValue(document.getElementById('val-avglos-3'), D.kpis.avgLOS, '', ' days', 1);
        animateValue(document.getElementById('val-avgbill-3'), D.kpis.avgBilling, '$', '', 0);

        buildBarChart('chart-condition-bar', D.patientsByCondition, true, 0);
        buildBarChart('chart-avgbill-condition', D.avgBillingByCondition, true, 2, '$');
        buildDoughnutChart('chart-admission-type', D.admissionTypeDistribution, 0);
        buildDoughnutChart('chart-test-results', D.testResultsDistribution, 6);
        buildBarChart('chart-medication', D.medicationUsage, false, 1);
        buildBarChart('chart-los-condition', D.avgLOSByCondition, true, 3);
        buildHeatmap('heatmap-table', D.conditionVsTestResults);

        // ── PAGE 4: Billing & Revenue ──
        animateValue(document.getElementById('val-revenue-4'), D.kpis.totalRevenue, '$', '', 0);
        animateValue(document.getElementById('val-avgbill-4'), D.kpis.avgBilling, '$', '', 0);
        animateValue(document.getElementById('val-maxbill-4'), D.kpis.maxBilling, '$', '', 0);

        buildLineChart('chart-revenue-year-4', D.revenueByYear, '$');
        buildBarChart('chart-revenue-insurance', D.revenueByInsurance, true, 1, '$');
        buildBarChart('chart-revenue-condition', D.revenueByCondition, false, 0, '$');
        buildDoughnutChart('chart-revenue-admission', D.revenueByAdmissionType, 0);
        buildBarChart('chart-avgbill-age', D.avgBillingByAgeGroup, true, 2, '$');
        buildBarChart('chart-top-hospitals', D.topHospitalsByRevenue, true, 4, '$');
        buildBarChart('chart-billing-dist', D.billingDistribution, false, 0);

    } catch (error) {
        console.error('Dashboard load error:', error);
        document.getElementById('page-overview').innerHTML = `
            <div style="text-align:center;padding:60px 20px;">
                <h2 style="color:#FF5252;margin-bottom:12px;">Failed to load dashboard data</h2>
                <p style="color:#8FA3B8;">${error.message}</p>
                <p style="color:#6B8299;margin-top:8px;">Make sure dashboard_data.json is in the same directory.</p>
            </div>
        `;
    }
}

// ── Initialize ──
document.addEventListener('DOMContentLoaded', loadDashboard);
