<script>
	import { onMount } from 'svelte';
	import Chart from 'chart.js/auto';
	import 'chartjs-adapter-date-fns';

	export let chartData;
	export let dataTypes;

	const titleMap = {
		pm10: 'PM10',
		pm2_5: 'PM2.5',
		reducing: 'Reducing',
		oxidising: 'Oxidising'
	};

	const textWhite = '#d4d4d8';
	const gridGrey = '#52525b';
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
	let datasets = [];
	dataTypes.forEach((dataType) => {
		datasets.push({
			label: titleMap[dataType],
			data: chartData['hoursInfo'].map((x) => x[dataType]),
			borderWidth: 1,
			fill: true,
			backgroundColor: backgroundColorMap[dataType],
			borderColor: borderColorMap[dataType]
		});
	});
	const data = {
		labels: chartData['hoursInfo'].map((x) => x['timestamp']),
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
							hour: 'dd/LL hha'
						}
					},
					ticks: {
						maxTicksLimit: 3,
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
