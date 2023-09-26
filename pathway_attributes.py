# encoding: utf-8
import read_pathway_from_text as rpf
import node_position as nop
import interaction_position as ip

def main(file:str):
    # テキストデータを読み込む
    # Todo: rpdを修正したデータファイルの形式に合わせてアップデートする
    source_dict = rpf.main(file)
    for idx, inter in enumerate(source_dict['interactions']):
        anchors = [a['ID'] for a in source_dict['anchors']]
        source_dict['interactions'][idx]['has_anchor'] =\
            (inter['start_point'] in anchors) or (inter['end_point'] in anchors)
    print("source: ", source_dict)
    # 擬似グラフを作成し、ノードの座標を取得する
    node_position = nop.main(source_dict)
    print("node_position",node_position)
    # interactionのstart_point, end_pointの座標とRelXYを生成する
    interaction_position = ip.main(source_dict, node_position)
    print(interaction_position)





    max_x = max(p[0] for p in node_position.values())
    max_y = max(p[1] for p in node_position.values())

    pathway = { 'Pathway': {
                   'Name': source_dict['pathway']['name'],
                   'Organism': source_dict['pathway']['organism'],
                   'BoardWidth': max_x + 100,
                   'BoardHeight': max_y + 30,
                },
                'Nodes': [
                    {'TextLabel': n['Label'], 'GraphId': n['ID'], 'BiologicalType': n['BiologicalType'],
                    'CenterX': node_position[n['ID']][0], 'CenterY': node_position[n['ID']][1]}
                    for n in source_dict['nodes']
                ],
                'Interations': [
                    {'GraphId': i['ID'], 'BiologicalType': i['BiologicalType'],
                     'Points': [
                           {'X': interaction_position[i['ID']]['start_point']['x'],
                            'Y': interaction_position[i['ID']]['start_point']['y'],
                            'RelX': interaction_position[i['ID']]['start_point']['RelX'],
                            'RelY': interaction_position[i['ID']]['start_point']['RelY'],
                            'GraphRef': interaction_position[i['ID']]['start_point']['GraphRef']},
                           {'X': interaction_position[i['ID']]['end_point']['x'],
                            'Y': interaction_position[i['ID']]['end_point']['y'],
                            'RelX': interaction_position[i['ID']]['end_point']['RelX'],
                            'RelY': interaction_position[i['ID']]['end_point']['RelY'],
                            'GraphRef': interaction_position[i['ID']]['end_point']['GraphRef']},
                     ]}
                    for i in source_dict['interactions']
                ],
                'Anchors': [
                    {'Position': a['position'], 'GraphId': a['ID'], 'BiologicalType': a['BiologicalType']}
                    for a in source_dict['anchors']
                ]
            }

    # anchorの座標を生成する

    # ソースファイルより読み込んだ属性をdictに追加する


if __name__ == "__main__":
    main("sample/simple_metabolite_text.txt")