varying highp vec2 vTextureCoord;

uniform sampler2D uSampler;

void main() {
    gl_FragColor = vec4(0.25, 0.25, 0.25, 1.0);//texture2D(uSampler, vTextureCoord);
}
