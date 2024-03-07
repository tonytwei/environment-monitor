<script>
	import { onMount } from 'svelte';
	import Chart from 'chart.js/auto';
	import 'chartjs-adapter-date-fns';

	export let chartData;
	export let dataType;

	const titleMap = {
		pm10: 'PM10',
		pm2_5: 'PM2.5',
		reducing: 'Reducing',
		oxidising: 'Oxidising'
	};
	const unitsMap = {
		pm10: 'µg/m³',
		pm2_5: 'µg/m³',
		reducing: 'kΩ',
		oxidising: 'kΩ'
	};

	const textWhite = '#e4e4e7';
	const borderColorMap = {
		pm10: 'rgba(255, 99, 132, 1)',
		pm2_5: 'rgba(54, 162, 235, 1)',
		reducing: 'rgba(255, 206, 86, 1)',
		oxidising: 'rgba(75, 192, 192, 1)'
	};
	const backgroundColorMap = {
		pm10: 'rgba(255, 99, 132, 0.2)',
		pm2_5: 'rgba(54, 162, 235, 0.2)',
		reducing: 'rgba(255, 206, 86, 0.2)',
		oxidising: 'rgba(75, 192, 192, 0.2)'
	};

	let chart;
	const data = {
		labels: chartData['hoursInfo'].map((x) => x['timestamp']),
		datasets: [
			{
				label: dataType,
				data: chartData['hoursInfo'].map((x) => x[dataType]),
				borderWidth: 1,
				pointRadius: 0,
				fill: true,
				backgroundColor: backgroundColorMap[dataType],
				borderColor: borderColorMap[dataType]
			}
		]
	};
	const config = {
		type: 'line',
		data: data,
		options: {
			layout: {
				padding: {
					bottom: -20,
					left: -20
				}
			},
			plugins: {
				title: {
					display: true,
					text: '        ' + titleMap[dataType],
					color: textWhite
				},
				legend: {
					display: false
				}
			},
			scales: {
				y: {
					min: 0,
					max: dataType === 'pm10' || dataType === 'pm2_5' ? 150 : undefined,
					ticks: {
						display: false
					},
					grid: {
						display: false
					}
				},
				x: {
					type: 'time',
					ticks: {
						display: false
					},
					grid: {
						display: false
					}
				}
			}
		},
		plugins: [
			{
				beforeDraw: (chart) => {
					const ctx = chart.ctx;
					ctx.save();
					ctx.fillStyle = backgroundColorMap[dataType];
					ctx.fillRect(0, 0, chart.width, chart.height);
					ctx.restore();
				}
			},
			{
				afterDraw: (chart) => {
					const ctx = chart.ctx;
					ctx.save();
					ctx.textAlign = 'center';
					ctx.textBaseline = 'middle';
					ctx.fillStyle = textWhite;
					ctx.font = '40px Verdana';
					ctx.fillText(
						chartData['hoursInfo'][0][dataType] + unitsMap[dataType],
						chart.width / 2,
						chart.height / 2
					);
					ctx.restore();
				}
			}
		]
	};
	onMount(() => {
		const ctx = chart.getContext('2d');
		new Chart(ctx, config);
	});
</script>

<canvas bind:this={chart} />
