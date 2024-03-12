<script>
	import logo from '$lib/assets/logo.png';

	export let location;
	export let time;
	export let loading;
	export let showInfo;

	let timeOptions = ['72 Hours', '48 Hours', '24 Hours', '12 Hours'];
	let locationOptions = [
		'Melbourne',
		'Sydney',
		'London',
		'New York',
		'Paris',
		'Rio de Janeiro',
		'Tokyo',
		'Beijing'
	];
</script>

<div class="bg-zinc-800 flex flex-row items-center justify-between p-2">
	<div class="flex flex-row items-center gap-2">
		<img src={logo} alt="map logo" class="h-16" />
		<h1 class="font-semibold text-xl text-slate-200">Enviroment Monitor Dashboard</h1>
	</div>
	<div class="flex flex-row gap-2">
		<select
			bind:value={location}
			on:change={() => {
				loading = true;
				showInfo = false;
			}}
			class="bg-zinc-600 text-zinc-100 text-lg p-1 rounded-md"
		>
			{#each locationOptions as location}
				<option value={location}>{location}</option>
			{/each}
		</select>
		<select bind:value={time} class="bg-zinc-600 text-zinc-100 text-lg p-1 rounded-md">
			{#each timeOptions as time}
				<option value={time}>{time}</option>
			{/each}
		</select>
	</div>
</div>
