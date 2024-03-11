<script>
	import { onMount } from 'svelte';
	import Chart from 'chart.js/auto';
	import 'chartjs-adapter-date-fns';

	export let chartData;
	export let dataTypes;
	export let time;
	const titleMap = {
		pm10: 'PM10',
		pm2_5: 'PM2.5',
		no2: 'NO2',
		so2: 'SO2',
		co: 'CO',
		o3: 'O3'
	};

	const timeLengths = {
		'72 Hours': 72,
		'48 Hours': 48,
		'24 Hours': 24,
		'12 Hours': 12
	};
	const timeDisplayFormats = {
		'72 Hours': 'dd/LL',
		'48 Hours': 'dd/LL HH:mm',
		'24 Hours': 'dd/LL HH:mm',
		'12 Hours': 'dd/LL HH:mm'
	};
	const timeTicks = {
		'72 Hours': 3,
		'48 Hours': 24,
		'24 Hours': 24,
		'12 Hours': 12
	};

	const textWhite = '#d4d4d8';
	const gridGrey = '#52525b';
	const borderColorMap = {
		pm10: 'rgba(255, 99, 132, 1)',
		pm2_5: 'rgba(54, 162, 235, 1)',
		no2: 'rgba(255, 206, 86, 1)',
		so2: 'rgba(75, 192, 192, 1)',
		co: 'rgba(153, 102, 255, 1)',
		o3: 'rgba(255, 159, 64, 1)'
	};
	const backgroundColorMap = {
		pm10: 'rgba(255, 99, 132, 0.2)',
		pm2_5: 'rgba(54, 162, 235, 0.2)',
		no2: 'rgba(255, 206, 86, 0.2)',
		so2: 'rgba(75, 192, 192, 0.2)',
		co: 'rgba(153, 102, 255, 0.2)',
		o3: 'rgba(255, 159, 64, 0.2)'
	};

	let chart;
	let datasets = [];
	dataTypes.forEach((dataType) => {
		let dataTypeSet = [];
		for (let i = 0; i < timeLengths[time]; i++) {
			dataTypeSet.push(chartData['hoursInfo'][i][dataType]);
		}
		datasets.push({
			label: titleMap[dataType],
			data: dataTypeSet,
			borderWidth: 1,
			fill: true,
			backgroundColor: backgroundColorMap[dataType],
			borderColor: borderColorMap[dataType]
		});
	});
	let dataLabels = [];
	for (let i = 0; i < timeLengths[time]; i++) {
		dataLabels.push(chartData['hoursInfo'][i]['timestamp']);
	}
	const data = {
		labels: dataLabels,
		datasets: datasets
	};
	const config = {
		type: 'line',
		data: data,
		options: {
			plugins: {
				legend: {
					labels: {
						color: textWhite
					}
				}
			},
			scales: {
				y: {
					min: 0,
					ticks: {
						color: textWhite
					},
					grid: {
						color: gridGrey
					}
				},
				x: {
					type: 'time',
					time: {
						unit: 'hour',
						displayFormats: {
							hour: timeDisplayFormats[time]
						}
					},
					ticks: {
						maxTicksLimit: timeTicks[time],
						color: textWhite
					},
					grid: {
						color: gridGrey
					}
				}
			}
		}
	};
	onMount(() => {
		const ctx = chart.getContext('2d');
		new Chart(ctx, config);
	});
</script>

<canvas bind:this={chart} />
