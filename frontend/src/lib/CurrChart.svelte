<script>
	import { onMount } from 'svelte';
	import Chart from 'chart.js/auto';
	import 'chartjs-adapter-date-fns';

	export let data;
	export let dataType;
	const titleMap = {
		pm10: 'Inhalable Particulate Matter (PM10)',
		pm2_5: 'Fine Particulate Matter (PM2.5)',
		pm1: 'Ultrafine Particulate Matter (PM1)',
		no2: 'Nitrogen Dioxide (NO2)',
		so2: 'Sulfur Dioxide(SO2)',
		co: 'Carbon Monoxide (CO)',
		o3: 'Ozone (O3)',
		temperature: 'Temperature',
		pressure: 'Pressure',
		humidity: 'Humidity'
	};
	const unitsMap = {
		pm10: 'µg/m³',
		pm2_5: 'µg/m³',
		pm1: 'µg/m³',
		no2: 'ppb',
		so2: 'ppb',
		co: 'ppb',
		o3: 'ppb',
		temperature: '°C',
		pressure: 'hPa',
		humidity: '%'
	};

	const textWhite = '#e4e4e7';
	const borderColorMap = {
		pm10: 'rgba(255, 99, 132, 1)',
		pm2_5: 'rgba(54, 162, 235, 1)',
		pm1: 'rgba(255, 99, 132, 1)',
		no2: 'rgba(255, 206, 86, 1)',
		so2: 'rgba(75, 192, 192, 1)',
		co: 'rgba(153, 102, 255, 1)',
		o3: 'rgba(255, 159, 64, 1)',
		temperature: 'rgba(255, 99, 132, 1)',
		pressure: 'rgba(54, 162, 235, 1)',
		humidity: 'rgba(255, 206, 86, 1)'
	};
	const backgroundColorMap = {
		pm10: 'rgba(255, 99, 132, 0.2)',
		pm2_5: 'rgba(54, 162, 235, 0.2)',
		pm1: 'rgba(255, 99, 132, 0.2)',
		no2: 'rgba(255, 206, 86, 0.2)',
		so2: 'rgba(75, 192, 192, 0.2)',
		co: 'rgba(153, 102, 255, 0.2)',
		o3: 'rgba(255, 159, 64, 0.2)',
		temperature: 'rgba(255, 99, 132, 0.2)',
		pressure: 'rgba(54, 162, 235, 0.2)',
		humidity: 'rgba(255, 206, 86, 0.2)'
	};

	let chart;
	const formattedData = {
		labels: data['hoursInfo'].map((x) => x['timestamp']),
		datasets: [
			{
				label: dataType,
				data: data['hoursInfo'].map((x) => x[dataType]),
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
		data: formattedData,
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
					max: dataType === 'pm10' || dataType === 'pm2_5' || dataType === 'pm1' ? 150 : undefined,
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
						data['hoursInfo'][0][dataType] + unitsMap[dataType],
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
