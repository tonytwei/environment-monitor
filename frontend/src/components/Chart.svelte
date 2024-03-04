<script>
	import { onMount } from 'svelte';
	import Chart from 'chart.js/auto';
	import 'chartjs-adapter-date-fns';

	export let chartData;
	export let dataType;

	let chart;
	const data = {
		labels: chartData['hoursInfo'].map((x) => x['timestamp']),
		datasets: [
			{
				label: dataType,
				data: chartData['hoursInfo'].map((x) => x[dataType]),
				borderWidth: 1
			}
		]
	};
	const config = {
		type: 'line',
		data: data,
		options: {
			scales: {
				y: {
					beginAtZero: true
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
						maxTicksLimit: 9
					}
				}
			},
			plugins: {
				customCanvasBackgroundColor: {
					color: 'lightGreen'
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
