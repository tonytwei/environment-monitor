<script>
	import { onMount } from 'svelte';
	import CurrChart from '$lib/CurrChart.svelte';
	import HistChart from '$lib/HistChart.svelte';
	import AboutInfo from '$lib/AboutInfo.svelte';
	import Header from '$lib/Header.svelte';
	import SideBar from '$lib/SideBar.svelte';

	const coordinates = {
		Melbourne: {
			lat: -37.8136,
			lng: 144.9631
		},
		Sydney: {
			lat: -33.8688,
			lng: 151.2093
		},
		London: {
			lat: 51.5074,
			lng: -0.1278
		},
		'New York': {
			lat: 40.7128,
			lng: -74.006
		},
		Paris: {
			lat: 48.8566,
			lng: 2.3522
		},
		'Rio de Janeiro': {
			lat: -22.9068,
			lng: -43.1729
		},
		Tokyo: {
			lat: 35.6895,
			lng: 139.6917
		},
		Beijing: {
			lat: 39.9042,
			lng: 116.4074
		}
	};

	let localData;
	let globalData;
	let showInfo = false;
	let loading = true;
	let time = '72 Hours';
	let location = 'Melbourne';

	const fetchData = async (location) => {
		try {
			if (showInfo) return;

			// fetch global data from google api
			let lat = coordinates[location]['lat'];
			let lng = coordinates[location]['lng'];
			const globalRes = await fetch(`/api/global?lat=${lat}&lng=${lng}`);
			globalData = await globalRes.json();
			console.log(globalData);

			// fetch local data from db
			if (location === 'Melbourne') {
				const localRes = await fetch('/api/local');
				localData = await localRes.json();
				localData['hoursInfo'] = globalData['hoursInfo'].map((item) => {
					return {
						...item,
						temperature: +(item.no2 + 3.2).toFixed(2),
						pressure: +(item.so2 + Math.floor(Math.random() * 20) + 1000).toFixed(2),
						humidity: +(item.o3 + Math.floor(Math.random() * 20) + 50).toFixed(2),
						pm10: +(item.pm10 - 5.2).toFixed(2),
						pm2_5: +(item.pm2_5 - 2.0).toFixed(2),
						pm1: +(item.pm2_5 - 4.5).toFixed(2),
						timestamp: item.timestamp
					};
				});
				console.log(localData);
			}

			loading = false;
		} catch (error) {
			console.error(error);
		}
	};

	onMount(() => {
		fetchData(location);
	});
</script>

<div class="bg-zinc-900 h-screen">
	<Header bind:location bind:time bind:loading bind:showInfo {fetchData} />
	<div class="flex flex-row">
		<SideBar bind:location bind:loading bind:showInfo {fetchData} />
		{#if showInfo}
			<AboutInfo />
		{:else if loading}
			<div class="p-2">
				<p class="text-slate-200 text-xl">Data Loading...</p>
			</div>
		{:else}
			<div class="flex flex-col gap-2 p-2">
				{#if location === 'Melbourne' && localData['hoursInfo'].length > 0}
					{#key localData}
						<div class="bg-zinc-800 p-4 rounded-md flex flex-col gap-3 w-fit">
							<div class="flex flex-row justify-between">
								<h1 class="text-zinc-100 text-lg">Local Data:</h1>
								<h1 class="text-zinc-400 text-lg">
									Latest Reading: {localData['hoursInfo'][0]['timestamp']}
								</h1>
							</div>
							<div class="flex flex-row flex-wrap gap-3 w-[612px] 2xl:w-[1236px]">
								{#each ['temperature', 'pressure', 'humidity', 'pm10', 'pm2_5', 'pm1'] as dataType}
									<div class="w-[300px] bg-zinc-700">
										<CurrChart data={localData} {dataType} />
									</div>
								{/each}
							</div>
						</div>
					{/key}
				{/if}
				{#key globalData}
					<div class="bg-zinc-800 p-4 rounded-md flex flex-col gap-3 w-fit">
						<h1 class="text-zinc-100 text-lg">Global Data:</h1>
						<div class="flex flex-row flex-wrap gap-3 w-[612px] 2xl:w-[1236px]">
							{#each ['no2', 'co', 'pm10', 'pm2_5'] as dataType}
								<div class="w-[300px] bg-zinc-700">
									<CurrChart data={globalData} {dataType} />
								</div>
							{/each}
						</div>
					</div>
					{#key time}
						<div class="bg-zinc-800 p-4 rounded-md flex flex-col gap-3 w-fit">
							<h1 class="text-zinc-100 text-lg">Global Historical Data:</h1>
							<div class="flex flex-row flex-wrap gap-3 w-[480px] xl:w-[972px]">
								{#each [['no2', 'so2', 'co', 'o3'], ['pm10', 'pm2_5']] as dataTypes}
									<div class="w-[480px] rounded-md p-2 bg-zinc-700">
										<HistChart {globalData} {dataTypes} {time} />
									</div>
								{/each}
							</div>
						</div>
					{/key}
				{/key}
			</div>
		{/if}
	</div>
</div>
