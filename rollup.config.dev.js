import buildConfig from './rollup.config';


const config = Array.isArray(buildConfig) ? buildConfig[0] : buildConfig;
Array.isArray(config.output) && (config.output = config.output[0]);

export default config;