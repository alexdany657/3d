attribute vec4 aVertexPosition;
attribute vec3 aVertexNormal;
attribute vec2 aTextureCoord;

uniform mat4 uNormalMatrix;
uniform mat4 uModelViewMatrix;
uniform mat4 uProjectionMatrix;

varying highp vec2 vTextureCoord;
varying highp vec3 vLighting;

void main() {
    gl_Position = uProjectionMatrix * uModelViewMatrix * aVertexPosition;
    vTextureCoord = aTextureCoord;

    highp vec3 ambientLight = vec3(0.3, 0.3, 0.3);

    highp vec3 directionalLightColor1 = vec3(0.3, 0.3, 0.3);
    highp vec3 directionalVector1 = normalize(vec3(-0.85, 0.8, 0.75));

    highp vec3 directionalLightColor2 = vec3(0.8, 0.8, 0.8);
    highp vec3 directionalVector2 = normalize(vec3(0.85, 0.8, 0.75));

    highp vec4 transformedNormal = uNormalMatrix * vec4(aVertexNormal, 1.0);
    
    highp float directional1 = max(dot(transformedNormal.xyz, directionalVector1), 0.0);
    highp float directional2 = max(dot(transformedNormal.xyz, directionalVector2), 0.0);

    vLighting = ambientLight + (directionalLightColor1 * directional1) + (directionalLightColor2 * directional2);
}
