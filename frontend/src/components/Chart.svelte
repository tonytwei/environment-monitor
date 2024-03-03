<script>
	import { onMount } from 'svelte';
	import Chart from 'chart.js/auto';
	import 'chartjs-adapter-date-fns';
	import { de } from 'date-fns/locale';

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
			}
		},
		adapters: {
			date: {
				locale: de
			}
		}
	};
	onMount(() => {
		const ctx = chart.getContext('2d');
		new Chart(ctx, config);
	});
</script>

<div class="h-72">
	<canvas bind:this={chart} />
</div>
